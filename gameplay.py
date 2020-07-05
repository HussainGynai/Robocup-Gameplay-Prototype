import classes
from typing import List, Set, Optional, Tuple, Type, TypeVar

OUR_ROBOTS = [1,2,3,4,5,6]
THEIR_ROBOTS = [7,8,9,10,11,12]


def get_gamestate() -> classes.GameState:
    return classes.GameState(OUR_ROBOTS, THEIR_ROBOTS, (0,0), classes.Possession.NEITHER) # would get from actual game_state

def play_selector(Situation: classes.Situation) -> classes.Play:
    for play in Situation.get_plays():
        if (play.cost(get_gamestate()) == 0):
            return play

def role_assignment(assignments: List[classes.TacticAssignment]) -> None:
    count = 0
    for assignment in assignments: # would be some eval function to properly assign robots
        assignment[0].assign_robot(OUR_ROBOTS[count]) 
        count = count + 1
        assignment[1].tick()
        """
        communicates to planning and rest of codebase which robots should do what through ROS
        """


SITUATIONS = [classes.BreakoutSituation()]

def gameplay():
    for situation in SITUATIONS:
        if situation.valid(get_gamestate()):
            play = play_selector(situation)
            current_situation = situation
            break 
    count = 0 
    while current_situation.valid(get_gamestate()) and count < 10:
        role_assignment(play.tick())
        count = count + 1

gameplay()



