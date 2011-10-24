#!/usr/bin/env python
'''
perceptron algorithm
if y(wx) <= 0
	w += nyx
will converge for classes which are linearly seperable
'''
import numpy
import sys
def perceptron(x=None, y=None, learning_rate=1):
	if not x or not y:
		return -1
	xmat = numpy.matrix(x)
	ymat = numpy.matrix(y)
	w = [0] * xmat.shape[1]
	wmat = numpy.matrix(w)
	flag_success = True
	current_iteration = 1
	while True:
		flag_success = True
		print 'Iteration: %d' % current_iteration
		current_iteration += 1
		for i in xrange(xmat.shape[0]):
			result = y[i] * numpy.linalg.det(wmat.transpose() * xmat[i])
			wmat += learning_rate * y[i] * xmat[i]
			if result <= 0:
				flag_success = False
		if flag_success:
			print wmat
			break
	return 0

if __name__ == '__main__':
	x = [[1, 3], [2, 3], [-3, 1], [1, -1]]
	y = [+1, -1, +1, -1]
	sys.exit(perceptron(x=x, y=y))
	
