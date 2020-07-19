import plays
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable

def get_context():
	return 1

def gameplay():
	play = plays.PassWithSeekers()
	for i in range(3):
		skills = play.tick()
		for action in skills:
			action.spin(get_context())

gameplay()
