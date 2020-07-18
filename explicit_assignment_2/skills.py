from classes import Role, Action, Skill
import actions
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable

class PivotKick(Skill):
	def __init__(self, role: Role, chip: Optional[bool] = False):
		self.role = role
		self.previous_role = None
		self.chip = chip
		self.game_state = None

	def tick(self) -> Action:
		self.capture = actions.Capture(self.role.robot)
		self.aim = actions.Aim(self.role.robot)
		if (not self.chip):
			self.kick = actions.Kick(self.role.robot)
		else:
			self.kick = actions.Chip(self.role.robot)
		yield self.capture
		yield self.aim
		yield self.kick

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role


class Recieve(Skill):
	def __init__(self, role: Role):
		self.role = role
		self.previous_role = None

	def tick(self) -> Action:
		self.move = actions.Move(self.role.robot)
		self.capture = actions.Capture(self.role.robot)
		yield self.move
		yield self.capture

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
		while(1):
			yield self.move

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role

class GoalieSkill(Skill):
	def __init__(self, role: Role):
		self.role = role
		self.previous_role = None

	def tick(self) -> Action:
		self.defend_goal = actions.GoalieAction(self.role.robot)
		while(1):
			yield self.defend_goal

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role
