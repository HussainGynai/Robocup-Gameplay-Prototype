from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable
from enum import Enum, auto
from abc import abstractmethod, ABC


class GameState:
    def __init__(self, our_robots, their_robots, ball, possession):
        self.our_robots = our_robots
        self.their_robots = their_robots
        self.ball = ball
        self.possession = possession
        # etc.

class Skill(ABC):
    def tick(self) -> None:
        ...

    def is_complete() -> bool:
        ...

class RolePriority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Role(ABC):

    def cost(self) -> float: #cost function for which which robot gets assigned the role
        ...

    def tick(self) -> Skill:
        ...

    def assign_robot(self, robot) -> None:
        ...

    def assign_priority(self, priority: RolePriority) -> None: #So plays/tactics can change priority
        ...

class Play(ABC):

    @abstractmethod
    def cost(self, game_state: GameState) -> float: #a cost function for choosing the play
        ...

    @abstractmethod
    def tick(self) -> List[Role]:
        ...

class Tactic(ABC):

    def tick(self) -> bool: #will check that all the roles it wants are assigned
        ...

class SeekTacticA(Tactic):

    def eval_seek() -> float:
        return 0

    class Seeker(Role):
        def __init__(self, priority: Optional[RolePriority] = None):
            self.robot = None
            self.priority = priority

        def cost(self) -> float:
            return 1

        def tick(self) -> Skill:
            return SeekSkill(SeekTacticA.eval_seek)

        def assign_priority(self, priority: RolePriority) -> None:
            self. priority = priority

        def assign_robot(self, robot) -> None:
            self.robot = robot
        """
        Not sure if roles should be created in tactics or outside of tactics
        If all roles go through sequential skill then it is also possible to just have 1 play class
        """

    def __init__(self):
        self.seeker = self.Seeker(RolePriority.LOW)

    def get_seeker(self) -> Role:
        return self.seeker

    def tick(self) -> bool:
        return self.seeker.robot is not None

class SeekSkill(Skill):

    def __init__(self, move_eval: Callable[...,float]):
        self.move_eval = move_eval 
    def tick(self) -> None:
        print('seeking')
        self.move_eval()

class Capture(Skill):
    def tick(self) -> None:
        print('capturing/recieving')

class PassTactic(Tactic):

    class Passer(Role):
        def __init__(self, heuristic, priority: Optional[RolePriority] = None):
            self.heuristic = heuristic
            self.robot = None
            self.priority = priority

        def cost(self) -> float:
            return 1

        def tick(self) -> Skill:
            return KickSkill(self.heuristic())

        def assign_priority(self, priority: RolePriority) -> None:
            self. priority = priority

        def assign_robot(self, robot) -> None:
            self.robot = robot

    class Reciever(Role):
        def __init__(self, priority: Optional[RolePriority] = None):
            self.robot = None
            self.priority = priority

        def cost(self) -> float:
            return 1

        def tick(self) -> Skill:
            return Capture()

        def assign_priority(self, priority: RolePriority) -> None:
            self.priority = priority

        def assign_robot(self, robot) -> None:
            self.robot = robot

    def __init__(self, heuristic):
        self.passer = self.Passer(heuristic, RolePriority.HIGH)
        self.reciever = self.Reciever(RolePriority.MEDIUM)

    def get_passer(self):
        return self.passer

    def get_reciever(self):
        return self.reciever

    def tick(self) -> bool:
        return self.passer.robot is not None and self.reciever.robot is not None


class KickSkill(Skill):
    step = 0
    def __init__(self, point, chip=False):
        self.chip = chip
        self.complete = False
        self.point = point

    def tick(self) -> None:
        KickSkill.step = KickSkill.step + 1
        if (KickSkill.step == 1):
            print('aiming')
        elif (KickSkill.step == 2):
            if (self.chip):
                print('chipping')
            else:
                print('kicking')
        else:
            print('kick complete')
            self.complete = True

    def is_complete(self):
        return self.complete

class GoalieSkill(Skill):
    def tick(self) -> None:
        print("defending goal")        

class GoalieTactic(Tactic):
    class Goalie(Role):
        def __init__(self, priority: Optional[RolePriority] = None):
            self.robot = None
            self.priority = priority

        def cost(self) -> float:
            return 1

        def tick(self) -> Skill:
            return GoalieSkill()

        def assign_priority(self, priority: RolePriority) -> None:
            self.priority = priority

        def assign_robot(self, robot) -> None:
            self.robot = robot

    def __init__(self):
        self.goalie = self.Goalie(RolePriority.HIGH)

    def get_goalie(self)-> Role:
        return self.goalie

    def tick(self) -> bool:
        return self.goalie.robot is not None

def pass_heuristic():
    pass

class PassToSeeker(Play):

    def cost(self, game_state: GameState) -> float:
        return 0

    def tick(self) -> None:
        """
        First create all tactics and roles to be used
        Change prioirties of roles if needed
        pass a list of roles into role_assignment()
        call tactic.tick() to check for assignment
        yield
        repeat
        """
        self.goalie_tactic = GoalieTactic()
        self.goalie = self.goalie_tactic.get_goalie()
        self.pass_tactic = PassTactic(pass_heuristic)
        self.passer = self.pass_tactic.get_passer()
        self.reciever = self.pass_tactic.get_reciever()
        self.seek_tactic1 = SeekTacticA()
        self.seek_tactic2 = SeekTacticA()
        self.seeker1 = self.seek_tactic1.get_seeker()
        self.seeker2 = self.seek_tactic2.get_seeker()
        from gameplay import role_assignment as role_assignment
        role_assignment([self.seeker1, self.seeker2, self.passer, self.goalie])
        self.seek_tactic1.tick()
        self.seek_tactic2.tick()
        yield
        role_assignment([self.seeker1, self.seeker2, self.passer, self.reciever, self.goalie])
        self.pass_tactic.tick()
        yield

