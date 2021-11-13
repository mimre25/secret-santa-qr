import qrcode
import random
import sys

names = sys.argv[1:]
mapping = [x for x in names]

def overlap(l1, l2):
	return any([a==b for a,b in zip(l1,l2)])

random.shuffle(mapping)
while overlap(names, mapping):
	random.shuffle(mapping)

for santa, santee in zip(mapping, names):
	img = qrcode.make(santee)
	img.save(f"{santa}.png")