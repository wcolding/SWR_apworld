from typing import Dict
import random

from BaseClasses import Item
from ..AutoWorld import World
from .Options import *
from .Items import *
from .Locations import *
from .Regions import *
from .ShopCosts import *

class SWRWorld(World):
    """
    Star Wars Episode I: Racer is a racing game where the player wins prize money and buys upgrades for their vehicle.
    This randomizer shuffles race rewards as well as shop items. It also randomizes track order and available racers.
    Now THIS is podracing!
    """
    game: str = "Star Wars Episode I Racer"
    topology_present = False
    options_dataclass = SWROptions
    options: SWROptions

    required_client_version = (0, 6, 0)

    item_name_to_id = get_item_name_to_id()
    location_name_to_id = get_location_name_to_id()
    
    item_name_groups = {
        "traction": {
            "Progressive Traction", "R-60 Repulsorgrip", "R-80 Repulsorgrip", "R-100 Repulsorgrip", "R-300 Repulsorgrip", "R-600 Repulsorgrip"
        },
        "turning": {
            "Progressive Turning", "Control Shift Plate", "Control Vectro Jet",  "Control Coupling", "Control Nozzle", "Control Stabilizer"
        },
        "acceleration": {
            "Progressive Acceleration", "44 PCX Injector", "Dual 32PCX Injector", "Quad 32PCX Injector", "Quad 44PCX Injector", "Mag-6 Injector"
        },
        "top speed": {
            "Progressive Top Speed", "Plug3 Thrust Coil", "Plug5 Thrust Coil", "Plug8 Thrust Coil", "Block5 Thrust Coil", "Block6 Thrust Coil"
        },
        "air brake": {
            "Progressive Air Brake", "Mark III Air Brake", "Mark IV Air Brake", "Mark V Air Brake", "Tri-Jet Air Brake", "Quadrijet Air Brake"
        },
        "cooling": {
            "Progressive Cooling", "Stack-3 Radiator", "Stack-6 Radiator", "Rod Coolant Pump", "Dual Coolant Pump", "Turbo Coolant Pump"
        },
        "repair": {
            "Progressive Repair", "Dual Power Cell", "Quad Power Cell", "Cluster Power Plug", "Rotary Power Plug", "Cluster2 Power Plug"
        },
        "amateur": {"Amateur Course Unlock"},
        "semi-pro": {"Semi-Pro Circuit Pass", "Semi-Pro Course Unlock"},
        "galactic": {"Galactic Circuit Pass", "Galactic Course Unlock"},
        "invitational": {"Invitational Circuit Pass", "Invitational Course Unlock"}
    }

    starting_racers_flag = 0
    randomized_courses = Dict[int, int]
    randomized_course_data = list()
    randomized_course_names = list()

    local_item_count = 0

    def set_shop_costs(self):
        self.shop_costs_data = dict()
        temp_costs = shop_costs_table[self.options.shop_costs.value]
        index_offset = 0
        for i in range(0, len(temp_costs)):
            if i % 5 == 0:
                index_offset += 1
            self.shop_costs_data.update({int(i + index_offset): int(temp_costs[i] * self.options.shop_cost_multiplier.value)})

    def set_starting_racers(self):
        self.racers_pool = dict(racers_table)

        if self.options.starting_racers == 0:
            # Vanilla
            for racer in vanilla_racers_list:
                self.starting_racers_flag |= self.racers_pool.pop(racer).bitflag
        else:
            # Random Range
            rand_range = self.options.starting_racers_count
            racer_names = [*racers_table]

            # Handle plando first
            if rand_range < len(self.options.starting_racers_plando.value):
                print("Unable to plando starting racers; list size exceeds Starting Racers Count value")
            else:
                for plando_racer in self.options.starting_racers_plando.value:
                    if plando_racer in racer_names:
                        racer_names.remove(plando_racer)
                        rand_range -= 1
                        self.starting_racers_flag |= self.racers_pool.pop(plando_racer).bitflag
                        print(f"Plando'd starting racer: {plando_racer}")
                    else:
                        print(f"Unable to plando racer: {plando_racer}\nNo matching racer name found")

            # Shuffle the remaining racers and pick from them
            random.shuffle(racer_names)
            
            for i in range(0, rand_range):
                selected_racer = racer_names.pop()
                self.starting_racers_flag |= self.racers_pool.pop(selected_racer).bitflag        

    def randomize_courses(self):
        self.randomized_courses = dict()
        self.randomized_course_data = list()
        self.randomized_course_names = list()

        course_entrances = [*course_clears_table]
        course_names = [*courses_table]
        mirrored_tracks = self.options.mirrored_tracks.value

        temp_courses = dict()

        # Handle plando first
        for plando_entry in self.options.course_plando.value.items():
            if plando_entry[0] in course_entrances:
                plando_course_name = plando_entry[1].replace(" (Mirrored)", "")
                if plando_course_name in course_names:
                    # Remove this entramce and course from the pool
                    course_names.remove(plando_course_name)
                    course_entrances.remove(plando_entry[0])

                    # Add this entry to the dict
                    index = get_course_entrance_index(plando_entry[0])
                    id = get_masked_course_id(plando_entry[1])
                    if (id & 0x80) != 0:
                        mirrored_tracks -= 1
                    temp_courses.update({index: id})
                else:
                    print(f"Could not plando course '{plando_entry[1]}'; no matching entry found")
            else:
                print(f"Could not plando course on location '{plando_entry[0]}'; no matching entry found")

        # Build course data of remaining courses
        for course in course_names:
            self.randomized_course_data += [SWRCourseData(course, courses_table[course])]

        random.shuffle(self.randomized_course_data)

        # Mirror any tracks not covered in plando
        if mirrored_tracks > 0:
            for i in range(0, mirrored_tracks):
                self.randomized_course_data[i].mirrored = True
            random.shuffle(self.randomized_course_data)

        # Fill in temp courses table with remaining course data
        index_offset = 0
        for current_course in self.randomized_course_data:
            if current_course.mirrored:
                current_course.id |= 0x80
            while index_offset in temp_courses.keys():
                index_offset += 1
            temp_courses.update({index_offset: current_course.id})
            index_offset += 1
            
        # Sort temp courses into the actual order
        for entry in sorted(temp_courses):
            self.randomized_courses.update({entry: temp_courses[entry]})

        # Populate course names list and spoiler log
        original_entrances = [*course_clears_table]
        course_keys = [*self.randomized_courses]
        for i in range(0, len(course_keys)):
            course_name = get_course_name_from_id(self.randomized_courses[course_keys[i]])
            self.randomized_course_names += [course_name]
            self.multiworld.spoiler.set_entrance(f"{original_entrances[i]}", course_name, 'entrance', self.player)

    def generate_early(self):
        self.set_starting_racers()
        self.randomize_courses()
        self.set_shop_costs()

    def fill_slot_data(self):
        return {
            "StartingRacers": self.starting_racers_flag,
            "Courses": self.randomized_courses,
            "ShopCosts": self.shop_costs_data,
            "ProgressiveParts": self.options.progressive_parts.value,
            "CourseUnlockMode": self.options.course_unlock_mode.value,
            "ProgressiveCircuits": self.options.progressive_circuits.value,
            "DisablePartDamage": self.options.disable_part_damage.value,
            "AIScaling": self.options.ai_scaling.value,
            "AdditionalAIMultiplier": self.options.additional_ai_multiplier.value,
            "EnableMultiplierControl": self.options.enable_multiplier_control.value,
            "OneLapMode": self.options.one_lap_mode.value,
            "AutoHintShop": self.options.auto_hint_shop.value,
            "DeathLinkAmnesty": self.options.deathlink_amnesty.value,
            "DeathLink": self.options.deathlink.value
        }
    
    def create_regions(self) -> None:
        return create_swr_regions(self)

    def create_item(self, name: str) -> Item:
        item_data = full_item_table[name]
        return SWRItem(name, item_data.classification, item_data.id, self.player)
    
    def append_items_from_data(self, name: str, count_override: int | None = None):
        item_data = full_item_table[name]
        count = item_data.max_allowed
        if count_override != None:
            if count_override < 1:
                return
            count = count_override

        self.local_item_count += count
        self.multiworld.itempool += [SWRItem(name, item_data.classification, item_data.id, self.player) for i in range(0, count)]

    def create_items(self) -> None:
        self.local_item_count = 0

        # Pod Parts
        parts_dict = dict(pod_upgrades_table)
        
        if self.options.progressive_parts:
            parts_dict = dict(pod_progressive_upgrades_table)
        
        if self.options.no_traction_upgrades:
            parts_dict.pop("Progressive Traction", None)
            parts_dict.pop("R-60 Repulsorgrip", None)
            parts_dict.pop("R-80 Repulsorgrip", None)
            parts_dict.pop("R-100 Repulsorgrip", None)
            parts_dict.pop("R-300 Repulsorgrip", None)
            parts_dict.pop("R-600 Repulsorgrip", None)

        for part in parts_dict:
            self.append_items_from_data(part)

        # Pit Droids
        if not self.options.disable_part_damage:
            self.append_items_from_data("Pit Droid")

        # Circuits
        if self.options.course_unlock_mode.value == 0:
            # Circuit Pass
            if self.options.progressive_circuits:
                self.append_items_from_data("Progressive Circuit Pass", 2)
            else:
                self.append_items_from_data("Semi-Pro Circuit Pass")
                self.append_items_from_data("Galactic Circuit Pass")

        if self.options.course_unlock_mode.value == 1:
            # Circuit Pass Invitational
            if self.options.progressive_circuits:
                self.append_items_from_data("Progressive Circuit Pass")
            else:
                self.append_items_from_data("Semi-Pro Circuit Pass")
                self.append_items_from_data("Galactic Circuit Pass")
                self.append_items_from_data("Invitational Circuit Pass")

        if self.options.course_unlock_mode.value == 2:
            # Shuffle
            self.append_items_from_data("Amateur Course Unlock", 6)
            self.append_items_from_data("Semi-Pro Course Unlock")
            self.append_items_from_data("Galactic Course Unlock")
            self.append_items_from_data("Invitational Course Unlock")
        
        # Racers
        racer_names = [*self.racers_pool]
        random.shuffle(racer_names)
        extra_racers = min(self.options.max_additional_racers.value, len(racer_names))
        for i in range(0, extra_racers):
            self.append_items_from_data(racer_names.pop())

        # Money
        for item in money_item_table:
            self.append_items_from_data(item)

        # Extra money to fill in gaps
        extra = len(self.multiworld.get_unfilled_locations(self.player)) - self.local_item_count
        if extra > 0:
            self.append_items_from_data("1000 Truguts", extra)

    def set_rules(self) -> None:
        return super().set_rules()