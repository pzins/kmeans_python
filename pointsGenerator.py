import random
# generate data for the kmeans algotihm

NUMBER = 1000000000
MAX = 5000
f = open("data.txt", "w")
for i in range(1000):
	x = random.randint(0, MAX)
	y = random.randint(0, MAX)
	f.write(str(x) + " " + str(y) + "\n")
