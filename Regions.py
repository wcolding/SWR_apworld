from BaseClasses import Region, Entrance, CollectionState
from ..generic.Rules import set_rule, CollectionRule
from ..AutoWorld import World
from .Locations import *
from .Items import course_unlocks_item_table

def create_swr_regions(world: World):
    menu_region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    # Circuits: Course clears, racer unlocks, and (optionally) course unlocks

    if world.options.course_unlock_mode == 2:
        create_circuit_region_with_course_shuffle(world, "Amateur Circuit", AMATEUR_CIRCUIT)
        create_circuit_region_with_course_shuffle(world, "Semi-Pro Circuit", SEMIPRO_CIRCUIT)
        create_circuit_region_with_course_shuffle(world, "Galactic Circuit", GALACTIC_CIRCUIT)
        create_circuit_region_with_course_shuffle(world, "Invitational Circuit", INVITATIONAL_CIRCUIT)

        create_region_with_rule(world, "Watto's Shop 0 Races", list(watto_0_races.keys()), lambda state: True)
        create_region_with_rule(world, "Watto's Shop 2 Races", list(watto_2_races.keys()), lambda state: has_enough_races_course_shuffle(state, world.player, 2))
        create_region_with_rule(world, "Watto's Shop 4 Races", list(watto_4_races.keys()), lambda state: has_enough_races_course_shuffle(state, world.player, 4))
        create_region_with_rule(world, "Watto's Shop 6 Races", list(watto_6_races.keys()), lambda state: has_enough_races_course_shuffle(state, world.player, 6))
        create_region_with_rule(world, "Watto's Shop 8 Races",  list(watto_8_races.keys()),  lambda state: has_enough_races_course_shuffle(state, world.player, 8))
        create_region_with_rule(world, "Watto's Shop 10 Races", list(watto_10_races.keys()), lambda state: has_enough_races_course_shuffle(state, world.player, 10))
        create_region_with_rule(world, "Watto's Shop 12 Races", list(watto_12_races.keys()), lambda state: has_enough_races_course_shuffle(state, world.player, 12))
        create_region_with_rule(world, "Watto's Shop 14 Races", list(watto_14_races.keys()), lambda state: has_enough_races_course_shuffle(state, world.player, 14))
        create_region_with_rule(world, "Watto's Shop 16 Races", list(watto_16_races.keys()), lambda state: has_enough_races_course_shuffle(state, world.player, 16))
    else:
        amateur_locations = get_circuit_locations(world, AMATEUR_CIRCUIT)
        semipro_locations = get_circuit_locations(world, SEMIPRO_CIRCUIT)
        galactic_locations = get_circuit_locations(world, GALACTIC_CIRCUIT)
        invitational_locations = get_circuit_locations(world, INVITATIONAL_CIRCUIT)

        create_region_with_rule(world, "Amateur Circuit", amateur_locations, lambda state: True)

        if world.options.progressive_circuits:
            create_region_with_rule(world, "Semi-Pro Circuit", semipro_locations, lambda state: state.has("Progressive Circuit Pass", world.player, 1))
            create_region_with_rule(world, "Galactic Circuit", galactic_locations, lambda state: state.has("Progressive Circuit Pass", world.player, 2))
        else:
            create_region_with_rule(world, "Semi-Pro Circuit", semipro_locations, lambda state: state.has("Semi-Pro Circuit Pass", world.player))
            create_region_with_rule(world, "Galactic Circuit", galactic_locations, lambda state: state.has("Galactic Circuit Pass", world.player))

        if world.options.course_unlock_mode == 1:
            if world.options.progressive_circuits:
                create_region_with_rule(world, "Invitational Circuit", invitational_locations, lambda state: state.has("Progressive Circuit Pass", world.player, 3))
            else:
                create_region_with_rule(world, "Invitational Circuit", invitational_locations, lambda state: state.has("Invitational Circuit Pass", world.player))
        else:
            # Player needs 1st place in all tracks in each preceding circuit to unlock the first three tracks in the invitation
            # For now we will treat it as all or nothing
            create_region_with_rule(world, "Invitational Circuit", invitational_locations, lambda state: state.has("Semi-Pro Circuit Pass", world.player) and state.has("Galactic Circuit Pass", world.player))

        # Shop
        create_region_with_rule(world, "Watto's Shop 0 Races", list(watto_0_races.keys()), lambda state: True)
        create_region_with_rule(world, "Watto's Shop 2 Races", list(watto_2_races.keys()), lambda state: True)
        create_region_with_rule(world, "Watto's Shop 4 Races", list(watto_4_races.keys()), lambda state: True)
        create_region_with_rule(world, "Watto's Shop 6 Races", list(watto_6_races.keys()), lambda state: True)

        if world.options.progressive_circuits:
            create_region_with_rule(world, "Watto's Shop 8 Races",  list(watto_8_races.keys()),  lambda state: state.has("Progressive Circuit Pass", world.player, 1))
            create_region_with_rule(world, "Watto's Shop 10 Races", list(watto_10_races.keys()), lambda state: state.has("Progressive Circuit Pass", world.player, 1))
            create_region_with_rule(world, "Watto's Shop 12 Races", list(watto_12_races.keys()), lambda state: state.has("Progressive Circuit Pass", world.player, 2))
            create_region_with_rule(world, "Watto's Shop 14 Races", list(watto_14_races.keys()), lambda state: state.has("Progressive Circuit Pass", world.player, 2))
            create_region_with_rule(world, "Watto's Shop 16 Races", list(watto_16_races.keys()), lambda state: state.has("Progressive Circuit Pass", world.player, 2))
        else:
            create_region_with_rule(world, "Watto's Shop 8 Races",  list(watto_8_races.keys()),  lambda state: has_enough_races(state, world.player, 8))
            create_region_with_rule(world, "Watto's Shop 10 Races", list(watto_10_races.keys()), lambda state: has_enough_races(state, world.player, 10))
            create_region_with_rule(world, "Watto's Shop 12 Races", list(watto_12_races.keys()), lambda state: has_enough_races(state, world.player, 12))
            create_region_with_rule(world, "Watto's Shop 14 Races", list(watto_14_races.keys()), lambda state: has_enough_races(state, world.player, 14))
            create_region_with_rule(world, "Watto's Shop 16 Races", list(watto_16_races.keys()), lambda state: has_enough_races(state, world.player, 16))

    create_region_with_rule(world, "Pit Droid Shop", list(pit_droid_shop_table.keys()), lambda state: True)  

    if world.options.course_unlock_mode == 0:
        if world.options.progressive_circuits:
            world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Circuit Pass", world.player, 2)
        else:
            world.multiworld.completion_condition[world.player] = \
                lambda state: state.has("Semi-Pro Circuit Pass", world.player) \
                and state.has("Galactic Circuit Pass", world.player)
    
    elif world.options.course_unlock_mode == 1:
        if world.options.progressive_circuits:
            world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Circuit Pass", world.player, 3)
        else:
            world.multiworld.completion_condition[world.player] = \
                lambda state: state.has("Semi-Pro Circuit Pass", world.player) \
                and state.has("Galactic Circuit Pass", world.player) \
                and state.has("Invitational Circuit Pass", world.player) 
            
    elif world.options.course_unlock_mode == 2:
        world.multiworld.completion_condition[world.player] = \
            lambda state: state.has("Amateur Course Unlock", world.player, 6) \
            and state.has("Semi-Pro Course Unlock", world.player, 7) \
            and state.has("Galactic Course Unlock", world.player, 7) \
            and state.has("Invitational Course Unlock", world.player, 4) \

def add_location_with_rule(world: World, region: Region, name: str, rule: CollectionRule) -> SWRLocation:
    new_loc = SWRLocation(world.player, name, full_location_table[name].id, region)
    set_rule(new_loc, rule)
    region.locations.append(new_loc)

def create_region_with_rule(world: World, name: str, location_names: list, rule: CollectionRule) -> Region:
    new_reg = Region(name, world.player, world.multiworld)
    for loc in location_names:
        add_location_with_rule(world, new_reg, loc, rule)

    world.multiworld.regions.append(new_reg)

    menu_region = world.multiworld.get_region("Menu", world.player)
    entrance = Entrance(world.player, name + "_ent", menu_region)
    entrance.access_rule = rule
    menu_region.exits.append(entrance)
    entrance.connect(new_reg)

def create_circuit_region_with_course_shuffle(world: World, name: str, circuit: int) -> Region:
    new_reg = Region(name, world.player, world.multiworld)
    required_item_name = [*course_unlocks_item_table][circuit]
    circuit_data = circuit_data_map[circuit]
    circuit_len = circuit_data.end - circuit_data.start
    
    for i in range(0, circuit_len):
        required_count = i 
        if (circuit != AMATEUR_CIRCUIT):
            required_count += 1

        # Clears / Money reward
        clear_name = [*circuit_data.clears_table][i]
        add_location_with_rule(world, new_reg, clear_name, lambda state: state.has(required_item_name, world.player, required_count))

        # Course Unlocks
        if i < len([*circuit_data.unlocks_table]):
            unlock_name = [*circuit_data.unlocks_table][i]
            add_location_with_rule(world, new_reg, unlock_name, lambda state: state.has(required_item_name, world.player, required_count))

        # Racer Unlocks
        course_name =  world.randomized_course_names[circuit_data.start + i]
        for loc in [*racer_unlocks_table]:
            if loc.removeprefix("Racer Unlock - ") in course_name:
                add_location_with_rule(world, new_reg, loc, lambda state: state.has(required_item_name, world.player, required_count)) 

    world.multiworld.regions.append(new_reg)

    menu_region = world.multiworld.get_region("Menu", world.player)
    entrance = Entrance(world.player, name + "_ent", menu_region)
    entrance.access_rule = lambda state: state.has(required_item_name, world.player)
    menu_region.exits.append(entrance)
    entrance.connect(new_reg)

def has_enough_races(state: CollectionState, player: int, required: int):
    count = 7
    if state.has("Semi-Pro Circuit Pass", player):
        count += 7
    
    if state.has("Galactic Circuit Pass", player):
        count += 7
        
    if state.has("Invitational Circuit", player):
        count += 4
        
    return count >= required

def has_enough_races_course_shuffle(state: CollectionState, player: int, required: int):
    count = 0
    for required_item in [*course_unlocks_item_table]:
        count += state.count(required_item, player)

    return count >= required

def get_matching_racer_unlocks(circuit_courses: list) -> list:
    unlocks = []
    for loc in racer_unlocks_table.keys():
        if loc.removeprefix("Racer Unlock - ") in circuit_courses:
            unlocks += [loc]
    return unlocks

def get_circuit_locations(world: World, circuit: int) -> list:
    circuit_data = circuit_data_map[circuit]
    locs = list(circuit_data.clears_table.keys())

    course_names = world.randomized_course_names[circuit_data.start:circuit_data.end]
    locs += get_matching_racer_unlocks(course_names)
    return locs