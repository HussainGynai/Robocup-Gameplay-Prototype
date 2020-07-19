from classes import Action
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable

class Kick(Action):
	def __init__(self, robot):
		self.robot = robot

	def spin(self, context) -> None:
		print("Robot #", self.robot, "is Kicking")

class Capture(Action):
	def __init__(self, robot):
		self.robot = robot

	def spin(self, context) -> None:
		print("Robot #", self.robot, "is Capturing")

class Move(Action):
	def __init__(self, robot):
		self.robot = robot

	def spin(self, context) -> None:
		print("Robot #", self.robot, "is Moving")

class LineKick(Action):
	def __init__(self, robot):
		self.robot = robot

	def spin(self, context) -> None:
		print("Robot #", self.robot, "is Line Kicking")

class Aim(Action):
	def __init__(self, robot):
		self.robot = robot

	def spin(self, context) -> None:
		print("Robot #", self.robot, "is Aiming")

class Chip(Action):
	def __init__(self, robot):
		self.robot = robot

	def spin(self, context) -> None:
		print("Robot #", self.robot, "is Chipping")

class GoalieAction(Action):
	def __init__(self, robot):
		self.robot = robot

	def spin(self, context) -> None:
		print("Robot #", self.robot, "is Defending the Goal")