from Options import Choice, Range, Toggle, DefaultOnToggle, DeathLink, dataclass, PerGameCommonOptions

class ProgressiveParts(Toggle):
    """Pod racer parts will always be the next level upgrade"""
    display_name = "Progressive Parts"

class ProgressiveCircuits(Toggle):
    """Access to circuits will be in the regular order"""
    display_name = "Progressive Circuits"
    
class EnableInvitationalCircuitPass(Toggle):
    """Affects how Invitational Circuit courses unlock. If enabled, Invitational is unlocked with a Circuit Pass item like the others. Otherwise, each Invitational course requires first place in all courses of a corresponding circuit."""
    display_name = "Invitational Circuit Pass"

class StartingRacers(Choice):
    """Change which racers are available to use at the beginning"""
    display_name = "Starting Racers"
    option_vanilla = 0
    option_random_range = 1

class StartingRacersCount(Range):
    """How many random racers to start with. This option is only used if Starting Racers is set to 'random_range'"""
    display_name = "Number of Starting Racers"
    range_start = 1
    range_end = 23
    default = 6

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
    """Prevents parts from being damaged and removes pit droids from the item pool. Extra money will be added to the pool."""
    display_name = "Disable Part Damage"

class OneLapMode(Toggle):
    """Races only require 1 lap to complete"""
    display_name = "1-Lap Mode"

@dataclass
class SWROptions(PerGameCommonOptions):
    progressive_parts: ProgressiveParts
    progressive_circuits: ProgressiveCircuits
    invitational_circuit_pass: EnableInvitationalCircuitPass
    starting_racers: StartingRacers
    starting_racers_count: StartingRacersCount
    disable_part_damage: DisablePartDamage
    ai_scaling: AIScaling
    additional_ai_multiplier: AdditionalAIMultiplier
    enable_multiplier_control: EnableMultiplierControl
    one_lap_mode: OneLapMode
    deathlink: DeathLink