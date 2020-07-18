from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable
from enum import Enum, auto
from abc import abstractmethod, ABC

class Role:
	def __init__(self):
		self.robot = None
		self.skill = None

	def assign_robot(self, robot: int) -> None:
		self.robot = robot


class Action(ABC):
	def spin(self) -> None:
		...

class Skill(ABC):

	def __init__(self, Role: Role):
		...

	def tick(self) -> Action:
		...

	def assign_role(self, role: Role):
		...

class RoleRequestPriority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class RoleRequest:
	def __init__(self, cost: Callable[...,float], constraints, priority: RoleRequestPriority, last_role: Optional[Role] = None):
		self.cost = cost
		self.constraints = constraints
		self.last_role = last_role
		self.role = Role()
		self.priority = priority

	def is_assigned(self) -> bool:
		return self.role.robot is not None

	def get_role(self) -> Role:
		return self.role

	def assign(self, robot) -> None:
		self.role.assign_robot(robot)

	def get_robot(self):
		return self.role.robot

class Tactic(ABC):
	def __init__(self):
		...

	def role_request(self) -> List[Role]:
		...

	def tick(self) -> List[Skill]:
		...

class Play(ABC):
	def __init__(self):
		...

	def tick(self) -> List[Skill]:
		...





