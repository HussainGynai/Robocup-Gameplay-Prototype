from enum import Enum

class Robot():
	def __init__(self, robot_id):
		self.robot_id = robot_id

class Role():
	def __init__(self, stateful_tags = None, stateless_tags = None, robot = None):
		self.robot = robot
		self.stateless_tags = stateless_tags
		self.stateful_tags = stateful_tags

	def assign_stateless(self, new_stateless_tags):
		self.stateless_tags = new_stateless_tags

	def assing_stateful(self, new_stateful_tags):
		self.stateful_tags = new_stateful_tags

	def assign_robot(robot):
		self.robot = robot

class ClearSituation():
	self.situation = 'clear' #would be of whatever type situational analysis returns

	class StatefulClearerTags(Enum):
		clearer = 1

	class StatelessClearerTags(Enum):
		has_ball = 1 #would actually be assigned by something else

	class StatefulReceiverTags(Enum):
		clear_receiver = 1

	class StatelessSeekingTags(Enum):
		clear_seeking = 1

	class StatelessGoalieTags(Enum):
		goalie = 1

	def get_play():
		return plays.clear.Clear() #would actually be play selector, would take in all stateful tags

	def __init__():
		self.play = get_play()
		self.clearer = Role(StatefulReceiverTags, StatelessClearerTags)
		self.clear_receiver = Role(StatefulReceiverTags)
		self.clear_seeker = Role()

	def tick():
		while (situation == situational_analysis()): #check if current situation is still valid
			self.clearer.assign_stateless(StatelessClearerTags)
			self.clear_receiver.assign_stateless(StatelessSeekingTags)
			self.clear_seeker.assign_stateless(StatelessSeekingTags)
			yield play.tick(self.clearer, self.clear_receiver, self.clear_seeker) #would yield into role assignment
		return None #return somehting to indicate a new situation has been reached




