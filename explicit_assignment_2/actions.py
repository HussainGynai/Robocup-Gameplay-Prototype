from classes import Action
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable

class Kick(Action):
	def spin(self, robot) -> None:
		print("Kicking")

class Capture(Action):
	def spin(self, robot) -> None:
		print("Capturing")

class Move(Action):
	def spin(self, robot) -> None:
		print("Moving")

class LineKick(Action):
	def spin(self, robot) -> None:
		print("Line Kicking")

class Aim(Action):
	def spin(self, robot) -> None:
		print("Aiming")

class Chip(Action):
	def spin(self, robot) -> None:
		print("Chipping")