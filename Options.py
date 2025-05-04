from Options import Choice, Range, Toggle, DefaultOnToggle, OptionSet, OptionDict, DeathLink, dataclass, PerGameCommonOptions

class ProgressiveParts(Toggle):
    """Pod racer parts will always be the next level upgrade"""
    display_name = "Progressive Parts"

class NoTractionUpgrades(Toggle):
    """Removes Traction parts from the item pool"""
    display_name = "No Traction Upgrades"

class ProgressiveCircuits(Toggle):
    """Access to circuits will be in the regular order
    Only applies when using Circuit Pass or Circuit Pass Invitational unlock modes"""
    display_name = "Progressive Circuits"
    
class CourseUnlockMode(Choice):
    """Sets how courses should unlock
    Circuit Pass: Semi-pro and Galactic Circuits are accessed by items called 'circuit passes'. Courses unlock normally as you beat the previous course
    Circuit Pass Invitational: Same as Circuit Pass but with the addition of the Invitational Circuit
    Shuffle: Course unlocks are shuffled
    """
    display_name = "Course Unlock Mode"
    option_circuit_pass = 0
    option_circuit_pass_invitational = 1
    option_shuffle = 2

class RandomizeStartingRacers(DefaultOnToggle):
    """Changes which racers are available to use at the beginning"""
    display_name = "Randomize Starting Racers"

class StartingRacersCount(Range):
    """How many random racers to start with
    This option is only used if 'Randomize Starting Racers' is enabled
    """
    display_name = "Number of Starting Racers"
    range_start = 1
    range_end = 23
    default = 6

class StartingRacersPlando(OptionSet):
    """List of specific racers with which to start
    This option is only used if 'Randomize Starting Racers' is enabled
    """
    display_name = "Starting Racers Plando"

class MaxAdditionalRacers(Range):
    """How many racers can be added to the pool (excluding the starting racers)"""
    display_name = "Max Additional Racers"
    range_start = 0
    range_end = 22
    default = 22

class MirroredTracks(Range):
    """How many tracks should be mirrored"""
    display_name = "Mirrored Tracks"
    range_start = 0
    range_end = 25
    default = 0

class AIScaling(Choice):
    """Affects AI speed
    Vanilla: Courses use their default scaling, which may result in tough races early on
    Circuits: AI is scaled according to the current circuit
    Parts: AI is dynamically scaled according to the quality of your parts
    """
    display_name = "AI Scaling"
    option_vanilla = 0
    option_circuits = 1 
    option_parts = 2
    default = 1

class AdditionalAIMultiplier(Range):
    """Applies additional scaling to AI
    1000 = 1.000
    """
    display_name = "Additional AI Multiplier"
    range_start = 100
    range_end = 5000
    default = 1000

class EnableMultiplierControl(DefaultOnToggle):
    """Allows the player to change the additional AI multiplier in-game"""
    display_name = "Enable Multiplier Control"

class DisablePartDamage(DefaultOnToggle):
    """Prevents parts from being damaged and removes pit droids from the item pool
    This does not remove the pit droid shop checks, just the pit droids themselves
    Extra money will be added to the pool to compensate
    """
    display_name = "Disable Part Damage"

class OneLapMode(Toggle):
    """Races only require 1 lap to complete"""
    display_name = "1-Lap Mode"

class AutoHintShop(Toggle):
    """Automatically hints shop items as they unlock"""
    display_name = "Auto-Hint Shop"

class DeathLinkAmnesty(Range):
    """Amount of times you can crash your pod before sending a DeathLink to the server"""
    display_name = "Death Link Amnesty"
    range_start = 0
    range_end = 50
    default = 0

class ShopCosts(Choice):
    """Sets the cost of items at Watto's shop
    Vanilla: Prices are unchanged. Some may require grinding truguts to afford
    Normalized: Prices are much closer together, with some categories being slightly more expensive than others
    Tiered: Each tier of any part type is an identical cost to that of other parts. This is the cheapest option
    """
    display_name = "Shop Costs"
    option_vanilla = 0
    option_normalized = 1
    option_tiered = 2

class ShopCostMultiplier(Range):
    """Additional multiplier for shop costs"""
    display_name = "Shop Cost Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class CoursePlando(OptionDict):
    """Sets specific courses
    For mirrored, append ' (Mirrored)' to any course name
    Repeated courses will cause errors"""
    display_name = "Course Plando"

@dataclass
class SWROptions(PerGameCommonOptions):
    progressive_parts: ProgressiveParts
    no_traction_upgrades: NoTractionUpgrades
    course_unlock_mode: CourseUnlockMode
    progressive_circuits: ProgressiveCircuits
    randomize_starting_racers: RandomizeStartingRacers
    starting_racers_count: StartingRacersCount
    starting_racers_plando: StartingRacersPlando
    max_additional_racers: MaxAdditionalRacers
    mirrored_tracks: MirroredTracks
    disable_part_damage: DisablePartDamage
    ai_scaling: AIScaling
    additional_ai_multiplier: AdditionalAIMultiplier
    enable_multiplier_control: EnableMultiplierControl
    one_lap_mode: OneLapMode
    auto_hint_shop: AutoHintShop
    shop_costs: ShopCosts
    shop_cost_multiplier: ShopCostMultiplier
    course_plando: CoursePlando
    deathlink_amnesty: DeathLinkAmnesty
    deathlink: DeathLink