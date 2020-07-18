import plays
from typing import List, Set, Optional, Tuple, Type, TypeVar, Callable

OUR_ROBOTS = [1,2,3,4,5,6]
THEIR_ROBOTS = 0


def gameplay():
	play = plays.PassWithSeekers().tick()
	for tactics in play:
		skills = []
		for tactic in tactics:
			skills = skills + tactic.__next__()
		for skill in skills:
			skill.__next__().spin()



gameplay()


# def test():
# 	count = 0
# 	for i in range(10):
# 		count = count + 1
# 		yield count


# test = test()
# for i in test:
# 	print(i)
