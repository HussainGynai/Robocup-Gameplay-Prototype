import plays
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable


def gameplay():
	play = plays.PassWithSeekers().tick()
	for tactics in play:
		skills = []
		for tactic in tactics:
			skills = skills + tactic.__next__()
		for skill in skills:
			skill.__next__().spin()



gameplay()
