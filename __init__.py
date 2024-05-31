from typing import Dict
import random

from BaseClasses import Item
from ..AutoWorld import World
from .Options import *
from .Items import *
from .Locations import *
from .Regions import *

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

    required_client_version = (0, 5, 2)

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
        "semi-pro": {"Semi-Pro Circuit Pass"},
        "galactic": {"Galactic Circuit Pass"},
        "invitational": {"Invitational Circuit Pass"}
    }

    racers_pool = racers_table
    starting_racers_flag = 0
    randomized_courses = Dict[int, int]
    randomized_course_data = list()
    randomized_course_names = list()

    local_item_count = 0

    def set_starting_racers(self):
        if self.options.starting_racers == 0:
            # Vanilla
            for racer in vanilla_racers_list:
                self.starting_racers_flag |= self.racers_pool.pop(racer).bitflag
        else:
            # Random Range
            rand_range = self.options.starting_racers_count
            racer_names = list(racers_table.keys())
            random.shuffle(racer_names)
            
            for i in range(0, rand_range):
                selected_racer = racer_names.pop()
                self.starting_racers_flag |= self.racers_pool.pop(selected_racer).bitflag        

    def randomize_courses(self):
        self.randomized_courses = {}
        course_clears = [*course_clears_table]
        course_names = [*courses_table]
        for i in range(0, len(course_names)):
            self.randomized_course_data += [SWRCourseData(course_names[i], courses_table[course_names[i]])]
        random.shuffle(self.randomized_course_data)

        if self.options.mirrored_tracks.value > 0:
            for i in range(0, self.options.mirrored_tracks.value):
                self.randomized_course_data[i].mirrored = True
            random.shuffle(self.randomized_course_data)

        # Set course data and spoiler log info
        for i in range(0, len(self.randomized_course_data)):
            current_course = self.randomized_course_data[i]
            if current_course.mirrored:
                current_course.id |= 0x80
                current_course.name += " (Mirrored)"
            self.randomized_courses.update({int(i): int(current_course.id)})
            self.multiworld.spoiler.set_entrance(f"{course_clears[i]} ({course_names[i]})", current_course.name, 'entrance', self.player)

    def generate_early(self):
        self.set_starting_racers()
        self.randomize_courses()

    def fill_slot_data(self):
        return {
            "StartingRacers": self.starting_racers_flag,
            "Courses": self.randomized_courses,
            "ProgressiveParts": self.options.progressive_parts.value,
            "CourseUnlockMode": self.options.course_unlock_mode.value,
            "ProgressiveCircuits": self.options.progressive_circuits.value,
            "DisablePartDamage": self.options.disable_part_damage.value,
            "AIScaling": self.options.ai_scaling.value,
            "AdditionalAIMultiplier": self.options.additional_ai_multiplier.value,
            "EnableMultiplierControl": self.options.enable_multiplier_control.value,
            "OneLapMode": self.options.one_lap_mode.value,
            "AutoHintShop": self.options.auto_hint_shop.value,
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
            count = count_override

        self.local_item_count += count
        self.multiworld.itempool += [SWRItem(name, item_data.classification, item_data.id, self.player) for i in range(0, count)]

    def create_items(self) -> None:
        # Pod Parts
        if self.options.progressive_parts:
            for part in pod_progressive_upgrades_table:
                self.append_items_from_data(part)
        else:
            for part in pod_upgrades_table:
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
        for racer in self.racers_pool:
            self.append_items_from_data(racer)

        # Money
        for item in money_item_table:
            self.append_items_from_data(item)

        # Extra money to fill in gaps
        extra = len(self.multiworld.get_unfilled_locations(self.player)) - self.local_item_count
        if extra > 0:
            self.append_items_from_data("1000 Truguts", extra)

    def set_rules(self) -> None:
        return super().set_rules()