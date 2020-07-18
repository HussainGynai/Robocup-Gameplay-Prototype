from classes import Role, Action, Skill, Tactic, RoleRequest, RoleRequestPriority, GameState
import actions
import skills



class Pass(Tactic):
	def __init__(self, passer_heurstic, receiver_heuristic):
		self.passer = RoleRequest(passer_heursitic, None, RoleRequestPriority.HIGH)
		self.receiever = RoleRequest(receiever_heuristic, None, RoleRequestPriority.HIGH)

	def role_request(self) -> List[Role]:
		return [self.passer, self.receiever]

	def tick(self) -> List[Skills]:
		if self.passer.is_assigned():
			