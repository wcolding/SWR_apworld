from BaseClasses import Region, Entrance, CollectionState
from ..generic.Rules import set_rule, CollectionRule
from ..AutoWorld import World
from .Locations import *

def create_swr_regions(world: World):
    menu_region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    # Circuits: Course clears and racer unlocks
    amateur_locations = get_circuit_locations(world, 0, 7)
    semipro_locations = get_circuit_locations(world, 7, 14)
    galactic_locations = get_circuit_locations(world, 14, 21)
    invitational_locations = get_circuit_locations(world, 21, 25)

    create_region_with_rule(world, "Amateur Circuit", amateur_locations, lambda state: True)
    
    if world.options.progressive_circuits:
        create_region_with_rule(world, "Semi-Pro Circuit", semipro_locations, lambda state: state.has("Progressive Circuit Pass", world.player, 1))
        create_region_with_rule(world, "Galactic Circuit", galactic_locations, lambda state: state.has("Progressive Circuit Pass", world.player, 2))
    else:
        create_region_with_rule(world, "Semi-Pro Circuit", semipro_locations, lambda state: state.has("Semi-Pro Circuit Pass", world.player))
        create_region_with_rule(world, "Galactic Circuit", galactic_locations, lambda state: state.has("Galactic Circuit Pass", world.player))

    if world.options.invitational_circuit_pass:
        if world.options.progressive_circuits:
            create_region_with_rule(world, "Invitational Circuit", invitational_locations, lambda state: state.has("Progressive Circuit Pass", world.player, 3))
        else:
            create_region_with_rule(world, "Invitational Circuit", invitational_locations, lambda state: state.has("Invitational Circuit Pass", world.player))
    else:
        # Player needs 1st place in all tracks in each preceding circuit to unlock the first three tracks in the invitation
        # For now we will treat it as all or nothing
        create_region_with_rule(world, "Invitational Circuit", invitational_locations, lambda state: state.can_reach("Semi-Pro Circuit", 'Region', world.player) and state.can_reach("Galactic Circuit", 'Region', world.player))

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

    if world.options.invitational_circuit_pass:
        if world.options.progressive_circuits:
            world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Circuit Pass", world.player, 3)
        else:
            world.multiworld.completion_condition[world.player] = \
                lambda state: state.has("Semi-Pro Circuit Pass", world.player) \
                and state.has("Galactic Circuit Pass", world.player) \
                and state.has("Invitational Circuit Pass", world.player) 
    else:
        if world.options.progressive_circuits:
            world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Circuit Pass", world.player, 2)
        else:
            world.multiworld.completion_condition[world.player] = \
                lambda state: state.has("Semi-Pro Circuit Pass", world.player) \
                and state.has("Galactic Circuit Pass", world.player)

def create_region_with_rule(world: World, name: str, location_names: list, rule: CollectionRule) -> Region:
    new_reg = Region(name, world.player, world.multiworld)
    for loc in location_names:
        loc_data = full_location_table[loc]
        new_loc = SWRLocation(world.player, loc, loc_data.id, new_reg)
        set_rule(new_loc, rule)
        new_reg.locations.append(new_loc)

    world.multiworld.regions.append(new_reg)

    menu_region = world.multiworld.get_region("Menu", world.player)
    entrance = Entrance(world.player, name + "_ent", menu_region)
    entrance.access_rule = rule
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

def get_matching_racer_unlocks(circuit_courses: list) -> list:
    unlocks = []
    for loc in racer_unlocks_table.keys():
        if loc.removeprefix("Racer Unlock - ") in circuit_courses:
            unlocks += [loc]
    return unlocks

def get_circuit_locations(world: World, start: int, end: int) -> list:
    clears = list(course_clears_table.keys())
    locs = clears[start:end]

    courses = world.randomized_course_names[start:end]
    locs += get_matching_racer_unlocks(courses)
    return locs