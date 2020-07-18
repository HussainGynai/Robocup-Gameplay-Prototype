from classes import Role, Action, Skill, GameState
import actions
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable

class PivotKick(Skill):
	def __init__(self, role: Role, chip: Optional[bool] = False):
		self.role = role
		self.previous_role = None
		self.chip = chip

	def tick(self, game_state: GameState) -> Action:
		self.capture = actions.Capture()
		self.aim = actions.Aim()
		if (not self.chip):
			self.kick = actions.Kick()
		else:
			self.kick = actions.Chip()
		yield self.capture
		yield self.aim
		yield self.kick

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role

class Recieve(Skill):
	def __init__(self, role: Role):
		self.role = role
		self.previous_role = previous_role

	def tick(self, game_state: GameState) -> Action:
		self.move = actions.Move()
		self.capture = actions.Capture()
		yield self.move
		yield self.capture

	def assign_role(self, role: Role) -> None:
		self.previous_role = self.role
		self.role = role

