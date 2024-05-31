from Options import Choice, Range, Toggle, DefaultOnToggle, DeathLink, dataclass, PerGameCommonOptions

class ProgressiveParts(Toggle):
    """Pod racer parts will always be the next level upgrade"""
    display_name = "Progressive Parts"

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

class StartingRacers(Choice):
    """Change which racers are available to use at the beginning"""
    display_name = "Starting Racers"
    option_vanilla = 0
    option_random_range = 1

class StartingRacersCount(Range):
    """How many random racers to start with
    This option is only used if Starting Racers is set to 'random_range'
    """
    display_name = "Number of Starting Racers"
    range_start = 1
    range_end = 23
    default = 6

class MirroredTracks(Range):
    """How many tracks should be mirrored"""
    display_name = "Mirrored Tracks"
    range_start = 0
    range_end = 25
    default = 0

class AIScaling(Choice):
    """Affects AI speed
    Vanilla: Courses use their default scaling
    Circuits: AI is scaled according to the current circuit
    Parts: AI is dynamically scaled according to the quality of your parts
    """
    display_name = "AI Scaling"
    option_vanilla = 0
    option_circuits = 1 
    option_parts = 2

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
    Extra money will be added to the pool
    """
    display_name = "Disable Part Damage"

class OneLapMode(Toggle):
    """Races only require 1 lap to complete"""
    display_name = "1-Lap Mode"

class AutoHintShop(Toggle):
    """Automatically hints shop items as they unlock"""
    display_name = "Auto-Hint Shop"

@dataclass
class SWROptions(PerGameCommonOptions):
    progressive_parts: ProgressiveParts
    course_unlock_mode: CourseUnlockMode
    progressive_circuits: ProgressiveCircuits
    starting_racers: StartingRacers
    starting_racers_count: StartingRacersCount
    mirrored_tracks: MirroredTracks
    disable_part_damage: DisablePartDamage
    ai_scaling: AIScaling
    additional_ai_multiplier: AdditionalAIMultiplier
    enable_multiplier_control: EnableMultiplierControl
    one_lap_mode: OneLapMode
    auto_hint_shop: AutoHintShop
    deathlink: DeathLink