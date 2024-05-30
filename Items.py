from BaseClasses import Item, ItemClassification

SWR_ITEM_OFFSET = 113800000

class SWRItem(Item):
    game: str = "Star Wars Episode I Racer"

class SWRItemData:
    def __init__(self, id: int | None, classification: ItemClassification, max_allowed: int = 1, bitflag: int | None = None):
        if id == None:
            self.id = None
        else:
            self.id = id + SWR_ITEM_OFFSET
        
        self.classification = classification
        self.max_allowed = max_allowed
        self.bitflag = bitflag

pod_progressive_upgrades_table = {
    "Progressive Traction":     SWRItemData(0, ItemClassification.useful, 5),
    "Progressive Turning":      SWRItemData(1, ItemClassification.useful, 5),
    "Progressive Acceleration": SWRItemData(2, ItemClassification.useful, 5),
    "Progressive Top Speed":    SWRItemData(3, ItemClassification.useful, 5),
    "Progressive Air Brake":    SWRItemData(4, ItemClassification.useful, 5),
    "Progressive Cooling":      SWRItemData(5, ItemClassification.useful, 5),
    "Progressive Repair":       SWRItemData(6, ItemClassification.useful, 5),
}

pod_upgrades_table = {
    # Traction
    "R-60 Repulsorgrip":   SWRItemData(7,  ItemClassification.useful),
    "R-80 Repulsorgrip":   SWRItemData(8,  ItemClassification.useful),
    "R-100 Repulsorgrip":  SWRItemData(9,  ItemClassification.useful),
    "R-300 Repulsorgrip":  SWRItemData(10, ItemClassification.useful),
    "R-600 Repulsorgrip":  SWRItemData(11, ItemClassification.useful),

    # Turning
    "Control Shift Plate": SWRItemData(12, ItemClassification.useful),
    "Control Vectro Jet":  SWRItemData(13, ItemClassification.useful),
    "Control Coupling":    SWRItemData(14, ItemClassification.useful),
    "Control Nozzle":      SWRItemData(15, ItemClassification.useful),
    "Control Stabilizer":  SWRItemData(16, ItemClassification.useful),

    # Acceleration
    "44 PCX Injector":     SWRItemData(17, ItemClassification.useful),
    "Dual 32PCX Injector": SWRItemData(18, ItemClassification.useful),
    "Quad 32PCX Injector": SWRItemData(19, ItemClassification.useful),
    "Quad 44PCX Injector": SWRItemData(20, ItemClassification.useful),
    "Mag-6 Injector":      SWRItemData(21, ItemClassification.useful),

    # Top Speed
    "Plug3 Thrust Coil":   SWRItemData(22, ItemClassification.useful),
    "Plug5 Thrust Coil":   SWRItemData(23, ItemClassification.useful),
    "Plug8 Thrust Coil":   SWRItemData(24, ItemClassification.useful),
    "Block5 Thrust Coil":  SWRItemData(25, ItemClassification.useful),
    "Block6 Thrust Coil":  SWRItemData(26, ItemClassification.useful),

    # Air Brake
    "Mark III Air Brake":  SWRItemData(27, ItemClassification.useful),
    "Mark IV Air Brake":   SWRItemData(28, ItemClassification.useful),
    "Mark V Air Brake":    SWRItemData(29, ItemClassification.useful),
    "Tri-Jet Air Brake":   SWRItemData(30, ItemClassification.useful),
    "Quadrijet Air Brake": SWRItemData(31, ItemClassification.useful),

    # Cooling
    "Stack-3 Radiator":    SWRItemData(32, ItemClassification.useful),
    "Stack-6 Radiator":    SWRItemData(33, ItemClassification.useful),
    "Rod Coolant Pump":    SWRItemData(34, ItemClassification.useful),
    "Dual Coolant Pump":   SWRItemData(35, ItemClassification.useful),
    "Turbo Coolant Pump":  SWRItemData(36, ItemClassification.useful),

    # Repair
    "Dual Power Cell":     SWRItemData(37, ItemClassification.useful),
    "Quad Power Cell":     SWRItemData(38, ItemClassification.useful),
    "Cluster Power Plug":  SWRItemData(39, ItemClassification.useful),
    "Rotary Power Plug":   SWRItemData(40, ItemClassification.useful),
    "Cluster2 Power Plug": SWRItemData(41, ItemClassification.useful),
}

racers_table = {
    "Anakin Skywalker":  SWRItemData(42, ItemClassification.filler, 1, 0x00000001),
    "Teemto Pagalies":   SWRItemData(43, ItemClassification.filler, 1, 0x00000002),
    "Sebulba":           SWRItemData(44, ItemClassification.filler, 1, 0x00000004),
    "Ratts Tyerell":     SWRItemData(45, ItemClassification.filler, 1, 0x00000008),
    "Aldar Beedo":       SWRItemData(46, ItemClassification.filler, 1, 0x00000010),
    "Mawhonic":          SWRItemData(47, ItemClassification.filler, 1, 0x00000020),
    "Ark 'Bumpy' Roose": SWRItemData(48, ItemClassification.filler, 1, 0x00000040),
    "Wan Sandage":       SWRItemData(49, ItemClassification.filler, 1, 0x00000080),

    "Mars Guo":          SWRItemData(50, ItemClassification.filler, 1, 0x00000100),
    "Ebe Endocott":      SWRItemData(51, ItemClassification.filler, 1, 0x00000200),
    "Dud Bolt":          SWRItemData(52, ItemClassification.filler, 1, 0x00000400),
    "Gasgano":           SWRItemData(53, ItemClassification.filler, 1, 0x00000800),
    "Clegg Holdfast":    SWRItemData(54, ItemClassification.filler, 1, 0x00001000),
    "Elan Mak":          SWRItemData(55, ItemClassification.filler, 1, 0x00002000),
    "Neva Kee":          SWRItemData(56, ItemClassification.filler, 1, 0x00004000),
    "Bozzie Baranta":    SWRItemData(57, ItemClassification.filler, 1, 0x00008000),

    "Boles Roor":        SWRItemData(58, ItemClassification.filler, 1, 0x00010000),
    "Ody Mandrell":      SWRItemData(59, ItemClassification.filler, 1, 0x00020000),
    "Fud Sang":          SWRItemData(60, ItemClassification.filler, 1, 0x00040000),
    "Ben Quadrinaros":   SWRItemData(61, ItemClassification.filler, 1, 0x00080000),
    "Slide Paramita":    SWRItemData(62, ItemClassification.filler, 1, 0x00100000),
    "Toy Dampner":       SWRItemData(63, ItemClassification.filler, 1, 0x00200000),
    "Bullseye Navior":   SWRItemData(64, ItemClassification.filler, 1, 0x00400000),
}

vanilla_racers_list = {
    "Anakin Skywalker",
    "Ebe Endocott",
    "Dud Bolt",
    "Gasgano",
    "Elan Mak",
    "Ody Mandrell"
}

misc_item_table = {
    "Pit Droid":                 SWRItemData(65, ItemClassification.useful, 3),
    "Semi-Pro Circuit Pass":     SWRItemData(66, ItemClassification.progression),
    "Galactic Circuit Pass":     SWRItemData(67, ItemClassification.progression),
    "Invitational Circuit Pass": SWRItemData(68, ItemClassification.progression),
    "Progressive Circuit Pass":  SWRItemData(69, ItemClassification.progression, 3),
}

# These are adjusted based on item trade in costs
# Races will be farmable and pay out "Fair" costs every time
# These values compensate for the difference between "Fair" and other payout choices
# In other words, races always pay out but these are the "vanilla rewards" for race completion that will be shuffled into the pool 
money_item_table = {
    "400 Truguts":               SWRItemData(70, ItemClassification.useful, 1),
    "600 Truguts":               SWRItemData(71, ItemClassification.useful, 2),
    "800 Truguts":               SWRItemData(72, ItemClassification.useful, 2),
    "1000 Truguts":              SWRItemData(73, ItemClassification.useful, 2),
    "1400 Truguts":              SWRItemData(74, ItemClassification.useful, 2),
    "2100 Truguts":              SWRItemData(75, ItemClassification.useful, 3),
    "2800 Truguts":              SWRItemData(76, ItemClassification.useful, 3),
    "3500 Truguts":              SWRItemData(77, ItemClassification.useful, 2),
}

course_unlocks_item_table = {
    "Amateur Course Unlock":      SWRItemData(78, ItemClassification.progression, 6),
    "Semi-Pro Course Unlock":     SWRItemData(79, ItemClassification.progression, 7),
    "Galactic Course Unlock":     SWRItemData(80, ItemClassification.progression, 7),
    "Invitational Course Unlock": SWRItemData(81, ItemClassification.progression, 4),
}

full_item_table = {
    **pod_progressive_upgrades_table,
    **pod_upgrades_table,
    **racers_table,
    **misc_item_table,
    **money_item_table,
    **course_unlocks_item_table
}

def get_item_name_to_id():
    item_name_to_id = dict()
    for item in full_item_table:
        item_name_to_id[item] = full_item_table[item].id
    return item_name_to_id