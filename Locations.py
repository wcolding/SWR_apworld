from BaseClasses import Location

SWR_LOC_OFFSET = 113800100


class SWRLocation(Location):
    game: str = "Star Wars Episode I Racer"
    is_course_clear: bool = False

class SWRLocationData:
    def __init__(self, id: int | None, required_races: int = 0):
        if id == None:
            self.id = None
        else:
            self.id = id + SWR_LOC_OFFSET
        self.required_races = required_races

watto_0_races = {
    "Watto's Shop - Traction Upgrade 1     (0 races)":     SWRLocationData(0, 0),
    "Watto's Shop - Turning Upgrade 1      (0 races)":      SWRLocationData(5, 0),
    "Watto's Shop - Acceleration Upgrade 1 (0 races)": SWRLocationData(10, 0),
    "Watto's Shop - Top Speed Upgrade 1    (0 races)":    SWRLocationData(15, 0),
    "Watto's Shop - Air Brake Upgrade 1    (0 races)":    SWRLocationData(20, 0),
    "Watto's Shop - Cooling Upgrade 1      (0 races)":      SWRLocationData(25, 0),
    "Watto's Shop - Repair Upgrade 1       (0 races)":       SWRLocationData(30, 0),
}

watto_2_races = {
    "Watto's Shop - Traction Upgrade 2     (2 races)":     SWRLocationData(1, 2),
    "Watto's Shop - Turning Upgrade 2      (2 races)":      SWRLocationData(6, 2),
    "Watto's Shop - Top Speed Upgrade 2    (2 races)":    SWRLocationData(16, 2),
    "Watto's Shop - Repair Upgrade 2       (2 races)":       SWRLocationData(31, 2),
}

watto_4_races = {
    "Watto's Shop - Acceleration Upgrade 2 (4 races)": SWRLocationData(11, 4),
    "Watto's Shop - Air Brake Upgrade 2    (4 races)":    SWRLocationData(21, 4),
    "Watto's Shop - Repair Upgrade 3       (4 races)":       SWRLocationData(32, 4),
}

watto_6_races = {
    "Watto's Shop - Traction Upgrade 3     (6 races)":     SWRLocationData(2, 6),
    "Watto's Shop - Turning Upgrade 3      (6 races)":      SWRLocationData(7, 6),
    "Watto's Shop - Air Brake Upgrade 3    (6 races)":    SWRLocationData(22, 6),
    "Watto's Shop - Cooling Upgrade 2      (6 races)":      SWRLocationData(26, 6),
}

watto_8_races = {
    "Watto's Shop - Acceleration Upgrade 3 (8 races)": SWRLocationData(12, 8),
    "Watto's Shop - Top Speed Upgrade 3    (8 races)":    SWRLocationData(17, 8),
    "Watto's Shop - Cooling Upgrade 3      (8 races)":      SWRLocationData(27, 8),
    "Watto's Shop - Repair Upgrade 4       (8 races)":       SWRLocationData(33, 8),
}

watto_10_races = {
    "Watto's Shop - Traction Upgrade 4     (10 races)":     SWRLocationData(3, 10),
    "Watto's Shop - Acceleration Upgrade 4 (10 races)": SWRLocationData(13, 10),
    "Watto's Shop - Air Brake Upgrade 4    (10 races)":    SWRLocationData(23, 10),
    "Watto's Shop - Cooling Upgrade 4      (10 races)":      SWRLocationData(28, 10),
}

watto_12_races = {
    "Watto's Shop - Turning Upgrade 4      (12 races)":      SWRLocationData(8, 12),
    "Watto's Shop - Acceleration Upgrade 5 (12 races)": SWRLocationData(14, 12),
    "Watto's Shop - Top Speed Upgrade 4    (12 races)":    SWRLocationData(18, 12),
    "Watto's Shop - Repair Upgrade 5       (12 races)":       SWRLocationData(34, 12),
}

watto_14_races = {
    "Watto's Shop - Traction Upgrade 5     (14 races)":     SWRLocationData(4, 14),
    "Watto's Shop - Air Brake Upgrade 5    (14 races)":    SWRLocationData(24, 14),
    "Watto's Shop - Cooling Upgrade 5      (14 races)":      SWRLocationData(29, 14),
}

watto_16_races = {
    "Watto's Shop - Turning Upgrade 5      (16 races)":      SWRLocationData(9, 16),
    "Watto's Shop - Top Speed Upgrade 5    (16 races)":    SWRLocationData(19, 16),
}

wattos_shop_table = {
    **watto_0_races,
    **watto_2_races,
    **watto_4_races,
    **watto_6_races,
    **watto_8_races,
    **watto_10_races,
    **watto_12_races,
    **watto_14_races,
    **watto_16_races    
}

# Junkyard has 7 slots (35-41)
# Reserve for if I figure out how to rework it ingame

pit_droid_shop_table = {
    "Pit Droid Shop - 1st Droid": SWRLocationData(42),
    "Pit Droid Shop - 2nd Droid": SWRLocationData(43),
    "Pit Droid Shop - 3rd Droid": SWRLocationData(44),
}

course_clears_table = {
    "Amateur Race 1":      SWRLocationData(45),
    "Amateur Race 2":      SWRLocationData(46),
    "Amateur Race 3":      SWRLocationData(47),
    "Amateur Race 4":      SWRLocationData(48),
    "Amateur Race 5":      SWRLocationData(49),
    "Amateur Race 6":      SWRLocationData(50),
    "Amateur Race 7":      SWRLocationData(51),

    "Semi-Pro Race 1":     SWRLocationData(52),
    "Semi-Pro Race 2":     SWRLocationData(53),
    "Semi-Pro Race 3":     SWRLocationData(54),
    "Semi-Pro Race 4":     SWRLocationData(55),
    "Semi-Pro Race 5":     SWRLocationData(56),
    "Semi-Pro Race 6":     SWRLocationData(57),
    "Semi-Pro Race 7":     SWRLocationData(58),

    "Galactic Race 1":     SWRLocationData(59),
    "Galactic Race 2":     SWRLocationData(60),
    "Galactic Race 3":     SWRLocationData(61),
    "Galactic Race 4":     SWRLocationData(62),
    "Galactic Race 5":     SWRLocationData(63),
    "Galactic Race 6":     SWRLocationData(64),
    "Galactic Race 7":     SWRLocationData(65),

    "Invitational Race 1": SWRLocationData(66),
    "Invitational Race 2": SWRLocationData(67),
    "Invitational Race 3": SWRLocationData(68),
    "Invitational Race 4": SWRLocationData(69),
}

racer_unlocks_table = {
    "Racer Unlock - Mon Gazza Speedway":  SWRLocationData(70),
    "Racer Unlock - The Boonta Classic":  SWRLocationData(71),
    "Racer Unlock - Howler Gorge":        SWRLocationData(72),
    "Racer Unlock - Beedo's Wild Ride":   SWRLocationData(73),
    "Racer Unlock - Andobi Mountain Run": SWRLocationData(74),

    "Racer Unlock - Bumpy's Breakers":    SWRLocationData(75),
    "Racer Unlock - Scrapper's Run":      SWRLocationData(76),
    "Racer Unlock - Spice Mine Run":      SWRLocationData(77),
    "Racer Unlock - Aquilaris Classic":   SWRLocationData(78),
    "Racer Unlock - Baroo Coast":         SWRLocationData(79),

    "Racer Unlock - Abyss":               SWRLocationData(80),
    "Racer Unlock - Zugga Challenge":     SWRLocationData(81),
    "Racer Unlock - Vengeance":           SWRLocationData(82),
    "Racer Unlock - Inferno":             SWRLocationData(83),
    "Racer Unlock - Ando Prime Centrum":  SWRLocationData(84),

    "Racer Unlock - Executioner":         SWRLocationData(85),
    "Racer Unlock - Sunken City":         SWRLocationData(86),
}

# Game Course IDs
courses_table = {
    "Boonta Training Course": 0x00,
    "Mon Gazza Speedway":     0x10,
    "Beedo's Wild Ride":      0x02,
    "Aquilaris Classic":      0x06,
    "Malastare 100":          0x16,
    "Vengeance":              0x13,
    "Spice Mine Run":         0x11,

    "Sunken City":            0x07,
    "Howler Gorge":           0x03,
    "Dug Derby":              0x17,
    "Scrapper's Run":         0x09,
    "Zugga Challenge":        0x12,
    "Baroo Coast":            0x0C,
    "Bumpy's Breakers":       0x08,

    "Executioner":            0x14,
    "Sebulba's Legacy":       0x18,
    "Grabvine Gateway":       0x0D,
    "Andobi Mountain Run":    0x04,
    "Dethro's Revenge":       0x0A,
    "Fire Mountain Rally":    0x0E,
    "The Boonta Classic":     0x01,
    
    "Ando Prime Centrum":     0x05,
    "Abyss":                  0x0B,
    "The Gauntlet":           0x15,
    "Inferno":                0x0F
}

full_location_table = {
    **wattos_shop_table,
    **pit_droid_shop_table,
    **course_clears_table,
    **racer_unlocks_table
}

def get_location_name_to_id():
    location_name_to_id = dict()
    for item in full_location_table:
        location_name_to_id[item] = full_location_table[item].id
    return location_name_to_id