# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class StartingCharacter(Choice):
    """Determine which character to start with."""
    display_name = "Starting Character"
    option_akiyama_shun = 0
    option_majima_goro = 1
    option_goda_ryuji = 2
    option_kiryu_kazuma = 3
    default = "random"

class SubstoryGoal(DefaultOnToggle):
    """Whether Substories should be required to Finish."""
    display_name = "Substory victory condition"

class TotalSubstories(Range):
    """If substory_goal is enabled, this defines the number of substories needed to win."""
    display_name = "Substory Total"
    range_start = 1
    range_end = 60
    default = 15

class GoldenGoal (Toggle):
    """Determines whether Golden Balls are required to finish. There are 7."""
    display_name = "Golden Ball Hunt"

class KaraokeSanity(Toggle):
    """Whether Karaoke tracks should be included as checks."""
    display_name = "Karaoke Sanity"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["starting_character"] = StartingCharacter
    options["substory_goal"] = SubstoryGoal
    options["golden_ball_hunt"] = GoldenGoal
    options["substory_completion"] = TotalSubstories
    options["karaoke_sanity"] = KaraokeSanity
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options