import classes
from typing import List, Set, Optional, Tuple, Type, TypeVar

OUR_ROBOTS = [1,2,3,4]
THEIR_ROBOTS = [7,8,9,10,11,12]



def play_selector() -> classes.Play:
    return classes.PassToSeeker()
    """
    Should just be normal situational analysis
    """

def get_priority(role: classes.Role) -> int: # a way to sort the priorities from the enums in each Role
    if (role.priority is classes.RolePriority.HIGH):
        return 1
    elif (role.priority is classes.RolePriority.MEDIUM):
        return 2
    else:
        return 3

def role_assignment(roles: List[classes.Role]) -> None:
    count = 0
    assigned_robots = []
    roles = sorted(list(roles), key=lambda role: get_priority(role))
    for role in roles: # would be some eval function to properly assign robots
        new_count = count
        while count < len(OUR_ROBOTS) and (OUR_ROBOTS[count] not in assigned_robots):
            role.assign_robot(OUR_ROBOTS[count])
            assigned_robots.append(OUR_ROBOTS[count])
            print('Robot', role.robot, end=': ')
            role.tick().tick()
            new_count = new_count + 1
            if new_count >= len(OUR_ROBOTS):
                break
        if new_count >= len(OUR_ROBOTS): #if we are out of robots then go back over the list using a lower priority replacement
            roles_rev = sorted(list(roles), key=lambda role: get_priority(role), reverse = True)
            for replacement in roles_rev:
                'here'
                if get_priority(replacement) > get_priority(role):
                    role.assign_robot(replacement.robot)
                    replacement.assign_robot(None)
        count = count + 1
        """
        communicates to planning and rest of codebase which robots should do what through ROS
        """

def gameplay():
    play = play_selector().tick()
    count = 0 #just here to make sure the demo doesn't last forevor
   
    while count < 2:
        print(play.__next__()) #tick through play
        count = count + 1


gameplay()