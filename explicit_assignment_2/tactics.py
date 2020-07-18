from classes import Role, Action, Skill, Tactic, RoleRequest, RoleRequestPriority
import actions
import skills
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable


class Pass(Tactic):
	def __init__(self, passer_heuristic, receiver_heuristic, chip: Optional[bool] = False):
		self.passer = RoleRequest(passer_heuristic, None, RoleRequestPriority.HIGH)
		self.receiever = RoleRequest(receiver_heuristic, None, RoleRequestPriority.HIGH)
		self.chip = chip
		self.role_requests = [self.passer, self.receiever]

	def role_request(self) -> List[Role]:
		return self.role_requests

	def tick(self) -> List[Skill]:
		self.pass_skill = skills.PivotKick(self.passer.get_role(), self.chip)
		self.receieve_skill = skills.Recieve(self.receiever.get_role())
		self.pass_gen = self.pass_skill.tick()
		self.receieve_gen = self.receieve_skill.tick()
		skill_list = []
		if self.passer.is_assigned():
			skill_list.append(self.pass_gen)
		yield skill_list
		skill_list = []
		if self.passer.is_assigned():
			skill_list.append(self.pass_gen)
		if self.receiever.is_assigned():
			skill_list.append(self.receieve_gen)
		yield skill_list
		skill_list = []
		if self.passer.is_assigned():
			skill_list.append(self.pass_gen)
		if self.receiever.is_assigned():
			skill_list.append(self.receieve_gen)
		yield skill_list
			
class SeekTactic(Tactic):
	def __init__(self, seek_selector, seeking_heuristic):
		self.seeker = RoleRequest(seek_selector, None, RoleRequestPriority.LOW)
		self.role_requests = [self.seeker]
		self.seeking_heuristic = seeking_heuristic

	def role_request(self) -> List[RoleRequest]:
		return self.role_requests

	def tick(self) -> List[Skill]:
		self.seek = skills.Seek(self.seeker.get_role(), self.seeking_heuristic)
		self.seek_gen = self.seek.tick()
		skill_list = []
		skill_list.append(self.seek_gen)
		while (1):
			yield skill_list

class GoalieTactic(Tactic):
	def __init__(self, goalie_selector):
		self.goalie = RoleRequest(goalie_selector, None, RoleRequestPriority.HIGH)
		self.role_requests = [self.goalie]

	def role_request(self) -> List[RoleRequest]:
		return self.role_requests

	def tick(self) -> List[Skill]:
		self.defend_goal = skills.GoalieSkill(self.goalie.get_role())
		self.goalie_gen = self.defend_goal.tick()
		skill_list = []
		skill_list.append(self.goalie_gen)
		while(1):
			yield skill_list 