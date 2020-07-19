from classes import Role, Action, Skill
import actions
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable
from enum import Enum, auto

class PivotKick(Skill):

	class State(Enum):
		capture = 1
		aim = 2
		kick = 3

	def __init__(self, role: Role, chip: Optional[bool] = False):
		self.role = role
		self.previous_role = None
		self.chip = chip
		self.game_state = None
		self.state = PivotKick.State.capture

	def tick(self) -> Action:
		self.capture = actions.Capture(self.role.robot)
		self.aim = actions.Aim(self.role.robot)
		if (not self.chip):
			self.kick = actions.Kick(self.role.robot)
		else:
			self.kick = actions.Chip(self.role.robot)
		if self.state == PivotKick.State.capture:
			self.state = PivotKick.State.aim
			return self.capture
		elif self.state == PivotKick.State.aim:
			self.state = PivotKick.State.kick
			return self.aim
		elif self.state == PivotKick.State.kick:
			return self.kick

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role


class Recieve(Skill):

	class State(Enum):
		move = 1
		recieve = 2

	def __init__(self, role: Role):
		self.role = role
		self.previous_role = None
		self.state = Recieve.State.move

	def tick(self) -> Action:
		self.move = actions.Move(self.role.robot)
		self.capture = actions.Capture(self.role.robot)
		if self.state == Recieve.State.move:
			return self.move
			self.state = Recieve.State.recieve
		if self.state == Recieve.State.recieve:
			return self.capture

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role

class Seek(Skill):
	def __init__(self, role: Role, seeker_heurstic):
		self.role = role
		self.previous_role = None
		self.seeker_heurstic = seeker_heurstic

	def tick(self) -> Action:
		self.move = actions.Move(self.role.robot)
		return self.move

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role

class GoalieSkill(Skill):
	def __init__(self, role: Role):
		self.role = role
		self.previous_role = None

	def tick(self) -> Action:
		self.defend_goal = actions.GoalieAction(self.role.robot)
		return self.defend_goal

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role
