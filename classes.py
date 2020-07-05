from typing import List, Set, Optional, Tuple, Type, TypeVar
from enum import Enum, auto
from abc import abstractmethod, ABC


class Tag:
    pass


class StatelessTag(Tag):
    pass


class StatefulTag(Tag):
    pass


class AttackerTag(StatelessTag):
    DEFAULT_AGGRESSION = 0.85

    def __init__(self, aggression: float = DEFAULT_AGGRESSION):
        """
        :param aggression: How aggressive this attacker is, from a scale of [0, 1].
        """
        self.aggression = aggression


class DefenderTag(StatelessTag):
    pass


class HasBallTag(StatelessTag):
    pass


class GoalieTag(StatelessTag):
    pass

class ClearSeekerTag(StatelessTag):
    pass
    """
    I think seekers should be stateless,
    not so sure about receivers though
    """

class ClearerTag(StatefulTag):
    pass 
    """
    could have data here like chip power or chip point,
    but those should be decided by the pass tactic I think
    """

class ClearRecieverTag(StatefulTag):
    pass

class Role:
    def __init__(self, stateless_tags: Set[StatelessTag],
                 stateful_tags: Optional[Set[StatefulTag]] = None):
        if stateful_tags is None:
            stateful_tags = set()

        self.stateless_tags = stateless_tags
        self.stateful_tags = stateful_tags
        self.robot = None

    def add_stateful_tag(self, stateful_tag: StatefulTag) -> None:
        self.stateful_tags.add(stateful_tag)

    def add_stateless_tag(self, stateless_tag: StatelessTag) -> None:
        self.stateless_tags.add(stateless_tag)

    def assign_robot(self, robot) -> None:
        self.robot = robot



class Possession(Enum):
    OURS = auto()
    THEIRS = auto()
    NEITHER = auto()


class GameState:
    def __init__(self, our_robots, their_robots, ball, possession: Possession):
        self.our_robots = our_robots
        self.their_robots = their_robots
        self.ball = ball
        self.possession = possession
        # etc.


class Situation(ABC):
    @abstractmethod
    def get_roles(self) -> List[Role]:
        ...

    @abstractmethod
    def valid(self, game_state: GameState) -> bool:
        ...

    @abstractmethod
    def cost(self, game_state: GameState) -> float:
        """ How good this situation is, normalized between [0, 1]
        :param game_state:
        :return:
        """
        ...


class BreakoutSituation(Situation):
    RISK_THRESHOLD = 0.45
    AGGRESSIVE_ATTACKER_AGGRESSION = 0.
    DEFENSIVE_ATTACKER_AGGRESSION = 0.3

    def get_roles(self) -> List[Role]:
        aggressive_attacker = Role({AttackerTag(BreakoutSituation.AGGRESSIVE_ATTACKER_AGGRESSION)})
        defensive_attacker = Role({AttackerTag(BreakoutSituation.DEFENSIVE_ATTACKER_AGGRESSION)})
        has_ball = Role({HasBallTag()})
        defender = Role({DefenderTag()})
        goalie = Role({GoalieTag()})

        return [
            aggressive_attacker,
            defensive_attacker,
            defensive_attacker,
            has_ball,
            defender,
            goalie
        ]

    def get_plays(self):
        return [Clear()]

    def valid(self, game_state: GameState) -> bool:
        """ This situation is only valid if we have the ball and the ball is in our half.
        :param game_state:
        :return:
        """
        free_ball = game_state.possession == Possession.NEITHER
        in_our_half = game_state.ball[1] <= 0
        return free_ball and in_our_half

    def cost(self, game_state: GameState) -> float:
        """ This situation is applicable if the risk of a turnover happening isn't high. If there is a high
        chance of a turnover, then the DefensiveKeepawaySituation is more applicable.
        :param game_state:
        :return:
        """
        return evaluation.our_turnover_risk(game_state)

class TacticPriority(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()


class Skill(ABC):
    def tick(self) -> None:
        ...


class Tactic(ABC):
    def tick(self) -> Skill:
        ...

TacticAssignment = Tuple[Role, Tactic]


class Roles:
    T = TypeVar('T', bound=Tag)

    def get(self, tag_class: Type[T]) -> List[Role]:
        ...


class Play(ABC):
    @abstractmethod
    def requirements(self) -> List[Role]:
        ...

    @abstractmethod
    def cost(self, game_state: GameState) -> float:
        ...

    @abstractmethod
    def tick(self, roles: Roles) -> List[TacticAssignment]:
        ...


class SeekTacticA(Tactic):
    def tick(self) -> None:
        SeekSkill().tick()

class SeekSkill(Skill):
    def tick(self) -> None:
        print('seeking')

class PassTactic(Tactic):
    def tick(self):
        print("chip: ", end='')
        KickSkill().tick()


class KickSkill(Skill):
    step = 0
    def __init__(self, chip=False):
        self.chip = chip
        self.complete = False

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
        

class GoalieTactic(Tactic):
    def tick(self) -> None:
        print("defending goal")



class Clear(Play):
    def __init__(self):
        self.clearer = Role({HasBallTag(), AttackerTag()}, {ClearerTag()})
        self.goalie = Role({GoalieTag()})
        self.seeker1 = Role({AttackerTag(), ClearSeekerTag()})
        self.seeker2 = Role({AttackerTag(), ClearSeekerTag()})

    def requirements(self) -> List[Role]:
        return [self.clearer, self.goalie, self.seeker1, self.seeker2]

    def cost(self, game_state: GameState) -> float:
        return 0

    def tick(self) -> List[TacticAssignment]:
        return [(self.seeker1, SeekTacticA()), (self.seeker2, SeekTacticA()), (self.clearer, PassTactic()), (self.goalie, GoalieTactic())]



