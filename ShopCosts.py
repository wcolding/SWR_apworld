# All of these skip the base item slot, which is hidden by the client anyway

default_shop_costs = [ 
    400, 600, 1200, 2600, 6000,      # Traction
    400, 700, 1600, 3800, 7500,      # Turning
    2200, 5600, 7000, 10400, 14000,  # Acceleration
    2400, 6000, 14000, 17500, 20000, # Top Speed
    1400, 3600, 7000, 10400, 14000,  # Air Brake
    100, 300, 900, 2700, 5400,       # Cooling
    300, 800, 1400, 4000, 7000       # Repair
]

normalized_shop_costs = [
    400, 600, 1200, 2600, 6000,   # Traction
    400, 600, 1200, 2600, 6000,   # Turning
    600, 900, 1800, 3900, 9000,   # Acceleration
    800, 1200, 2400, 5200, 12000, # Top Speed
    600, 900, 1800, 3900, 9000,   # Air Brake
    400, 600, 1200, 2600, 6000,   # Cooling
    400, 600, 1200, 2600, 6000    # Repair
]

tiered_shop_costs = [400, 600, 800, 1000, 1200] * 7

shop_costs_table = {
    0: default_shop_costs,
    1: normalized_shop_costs,
    2: tiered_shop_costs
}