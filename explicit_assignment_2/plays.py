from classes import Role, Action, Skill, Tactic, Play, RoleRequest, RoleRequestPriority
import actions
import skills
import tactics
import role_assignment
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable


def seeking_heursitic():
	pass

def seeker_cost():
	pass

def passer_cost():
	pass

def receiver_cost():
	pass

def goalie_Cost():
	pass

class PassWithSeekers(Play):
	def __init__(self):
		self.pass_tactic = tactics.Pass(passer_cost, receiver_cost)
		self.seeker_tactic = tactics.SeekTactic(seeker_cost, seeking_heursitic)
		self.goalie_tactic = tactics.GoalieTactic(goalie_Cost)
		self.pass_gen = self.pass_tactic.tick()
		self.seek_gen = self.seeker_tactic.tick()
		self.goalie_gen = self.goalie_tactic.tick()

	def tick(self):
		for i in range(3):
			requests = []
			requests = requests + self.pass_tactic.role_request()
			requests = requests + self.seeker_tactic.role_request()
			requests = requests + self.goalie_tactic.role_request()
			role_assignment.role_assigner(requests)
			skills_list = []
			skills_list.append(self.pass_gen)
			skills_list.append(self.seek_gen)
			skills_list.append(self.goalie_gen)
			yield skills_list