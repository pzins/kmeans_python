import time
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show

import time

class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

def euclidian(p, q):
	return math.sqrt(math.pow(p.x - q.x, 2) + math.pow(p.y - q.y, 2))

def loadData(filename):
	global data
	f = open(filename, "r")
	for line in f:
		tmp = line.split(' ')
		p = Point(int(tmp[0]), int(tmp[1]))
		if p not in data:
			data.append(p)


def printClusters():
	for i in range(len(liste)):
		print("------------------------------------")
		print("cluster n°" + str(i+1) + " ", end="")
		print(centroids[i])
		for j in liste[i]:
			print(j)
		print("------------------------------------")

def printCentroids():
	for i in centroids:
		print(i)

def calcDistTotal():
	total = 0
	for i in range(len(liste)):
		for j in liste[i]:
			total += euclidian(centroids[i], j)
	return total




def meanCluster(points):
	sumX, sumY = 0, 0
	size = len(points)
	for i in points:
		sumX += i.x
		sumY += i.y
	return Point(round(sumX / size), round(sumY / size))

def hasCentroidsMove(newCentroids, threshodld):
	for i in range(len(newCentroids)):
		if abs(centroids[i].x - newCentroids[i].x)  > threshodld or abs(centroids[i].y - newCentroids[i].y)  > threshodld:
			return True;
	return False

def findCluster():
	global liste
	liste = [[] for _ in range(k)]	
	for i in data:
		mini, indice = 100000, -1
		for c in range(len(centroids)):
			tmp = euclidian(centroids[c], i)
			if tmp < mini:
				mini = tmp
				indice = c
		liste[indice].append(i)
	print("#### dist total = " + str(calcDistTotal()))

def calcNewCentroids():
	global centroids
	newCentroids = []
	for i in range(len(liste)):
		if len(liste[i]) == 0:
			newCentroids.append(centroids[i])
		else:
			newCentroids.append(meanCluster(liste[i]))
	res = hasCentroidsMove(newCentroids, 1)
	centroids = newCentroids
	return res;


clusterColor = ["r", "b", "g", "y", "w", "c"]

def printData():
	plt.clf()
	for i in range(len(liste)):
		for j in liste[i]:
			plt.plot(j.x, j.y, 'ro', c=clusterColor[i%7])
	plt.axis([0, 5000, 0, 5000])
	for j in centroids:
		plt.plot(j.x, j.y, 'ro', c="k")

	plt.draw()



k = 6
data = []
loadData("data.txt")
centroids = [data[i] for i in range(k)]
liste = [[] for _ in range(k)]


start_time = time.time()
ion()
while True:
	findCluster()
	if not calcNewCentroids():
		break
	printData()
	# time.sleep(0.5)

print("--- %s seconds ---" % (time.time() - start_time))
