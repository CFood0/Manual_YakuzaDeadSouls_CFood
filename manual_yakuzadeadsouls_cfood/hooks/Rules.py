from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
#def overfishedAnywhere(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
#    """Has the player collected all fish from any fishing log?"""
#    for cat, items in world.item_name_groups:
#        if cat.endswith("Fishing Log") and state.has_all(items, player):
#            return True
#    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
#def anyClassLevel(world: World, multiworld: MultiWorld, state: CollectionState, player: int, level: str):
#    """Has the player reached the given level in any class?"""
#    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
#        if state.count(item, player) >= int(level):
#            return True
#    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
#def requiresMelee(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
#    """Returns a requires string that checks if the player has unlocked the tank."""
#    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def SubstoryTokens(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player finished enough substories?"""
    for item in ["Substory Token"]:
        if state.count(item, player) >= int(multiworld.worlds[player].options.substory_completion):
            return True
    return False

def defaultWinCon(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """If all win cons are disabled, does the player have the default alternative items?"""
    if multiworld.worlds[player].options.substory_goal == True:
        return True
    elif multiworld.worlds[player].options.golden_ball_hunt == True:
        return True
    else:
        return "|Kiryu Kazuma| and |Kiryu's Scenario Battles| and |Anti-tank Missile| and |Grenades|"