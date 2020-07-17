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

class Action(ABC):
	def run(self) -> None:
		...

class Skill(ABC):

	def __init__(self, Role: Role):
		...

	def tick(self, game_state: GameState) -> Action:
		...

	def is_role_changed(self) -> bool:
		...

class Role:
	def __init__(self):
		self.robot = None
		self.skill = None

	def assign_robot(self, robot: int) -> None:
		self.robot = robot

	def assign_skill(self, skill: Skill) -> None:
		self.skill = skill

class RoleRequest:
	def __init__(self, cost: Callable[...,float], constraints, last_role: Role):
		self.cost = cost
		self.constraints = constraints
		self.last_role = last_role
		self.role = Role()

	def is_assigned(self) -> bool:
		return self.role.robot is not None

class Tactic(ABC):
	def __init__(self):
		...

	def role_request(self) -> List[Role]:
		...

	def tick(self) -> List[Skills]:
		...

class Play(ABC):
	def __init__(self):
		...

	def tick(self) -> List[Role]:
		...





