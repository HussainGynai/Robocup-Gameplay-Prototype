from classes import Role, Action, Skill, Tactic, RoleRequest, RoleRequestPriority
import actions
import skills
import tactics
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable


OUR_ROBOTS = [1,2,3,4,5,6]

def get_priority(role_request: RoleRequestPriority) -> int: # a way to sort the priorities from the enums in each Role
    if (role_request.priority is RoleRequestPriority.HIGH):
        return 1
    elif (role_request.priority is RoleRequestPriority.MEDIUM):
        return 2
    else:
        return 3

def role_assigner(role_requests: List[RoleRequest]):
    count = 0
    assigned_robots = []
    requests = sorted(role_requests, key=lambda request: get_priority(request))
    for request in requests: # would be some eval function to properly assign robots
        new_count = count
        while count < len(OUR_ROBOTS) and (OUR_ROBOTS[count] not in assigned_robots):
            request.assign(OUR_ROBOTS[count])
            assigned_robots.append(OUR_ROBOTS[count])
            new_count = new_count + 1
            if new_count >= len(OUR_ROBOTS):
                break
        if new_count >= len(OUR_ROBOTS): #if we are out of robots then go back over the list using a lower priority replacement
            requests_rev = sorted(requests, key=lambda request: get_priority(request), reverse = True)
            for replacement in requests_rev:
                if get_priority(replacement) > get_priority(request):
                    request.assign(replacement.get_robot())
                    replacement.assign(None)
        count = count + 1