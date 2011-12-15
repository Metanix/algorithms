from __future__ import division
import random

class Instances(object):
	def __init__(self):
		self.weights = []
		self.instances = []
		self.classifier = []
		self.length = 0

	def add(self, instance):
		if self.weights == []:
			self.weights = [1]*len(instance[:-1])
		self.instances.append(instance[:-1])
		self.classifier.append(instance[-1])
		self.length += 1
	
	def update_weight(self, weight):
		self.weights = weight[:]

	def __len__(self):
		return len(self.instances)

	def __iter__(self):
		return self
	
	def next(self):
		if self.length == 0:
			raise StopIteration
		self.length -= 1
		total_length = len(self.instances)
		current_position = total_length - self.length - 1
		return (self.weights, self.instances[current_position], self.classifier[current_position])
		

def test(weight, feature, theta):
	if sum(weight[i] * feature[i] for i in xrange(len(feature))) > theta:
		return 1
	return 0

def winnow2(instances):
	theta = len(instances)/2
	alpha = 2
	correctly_classified = 0
	for current, instance in enumerate(instances):
		weight, features, classifier = instance
		result = test(weight, features,theta)
		if result != classifier:
			new_weight = weight[:]
			if result > 0:
				for i, w in enumerate(features):
					if w >= 1:
						new_weight[i] /= alpha
			else:
				for i, w in enumerate(features):
					if w >= 1:
						new_weight[i] *= alpha
			instances.update_weight(new_weight)
		else:
			correctly_classified += 1	
		value = correctly_classified / (current + 1)
		print weight, value

instances = Instances()
def circle(x,y,r,p):
	l = [i/100 for i in range(100)]
	m = [(abs(r-(l[i]-x)**2))**.5 - y for i in xrange(100)]
	return [(l[i], m[i], p) for i in xrange(100)]

a = []
for item in circle(-2,-4,1,1):
	a.append(item)
for item in circle(2, 4, 1, 0):
	a.append(item)
random.shuffle(a)
for item in a:
	instances.add(item)

winnow2(instances)
