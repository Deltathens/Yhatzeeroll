
import random

def dicroll(dic):
    fnl = []
    rlst = []
	for iter in range(0, dic):
		gen = str(random.randint(1, 6))
		rlst.append(gen)
	fnl.append(rlst)
	return fnl

def yhatloop(lim):
	Yhatroll = False
	rolcount = 0
	while not Yhatroll:
		roll = dicroll(6)
		if rolcount == lim:
			break
		else:
			if roll = [['1'] * 5]:
				rolcount += 1
				Yhatroll = True
			elif roll = [['2'] * 5]:
				rolcount += 1
				Yhatroll = True
			elif roll = [['3'] * 5]:
				rolcount += 1
				Yhatroll = True
			elif roll = [['4'] * 5]:
				rolcount += 1
				Yhatroll = True
			elif roll = [['5'] * 5]:
				rolcount += 1
				Yhatroll = True
			elif roll = [['6'] * 5]:
				rolcount += 1
				Yhatroll = True
			else:
				rolcount += 1
	if Yhatroll = True:
		print(roll, rolcount, "YHATZEE!")
	else:
		print(roll, rolcount)
yhatloop(1296)
