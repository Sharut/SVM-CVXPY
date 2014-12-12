
from cvxpy import *

import numpy

class svm(object):
	def __init__(self,M,weighted = False):
		self.M = M
		self.W = numpy.random.randn(M,1)
		self.ready = False
		self.weighted = weighted

	def train(self,X,Y):
		
		if len(X) != len(Y):
			print 'Error: the numbers of inputs and outputs donot match!'
			return
		A = []
	
		for k in xrange(len(Y)):
			temp = list(X[k])
			if Y[k][0] == 1:
				temp.append(1)
				A.append(temp)
				
			else:
				temp = [(-1)*v for v in temp]
				temp.append(-1)
				A.append(temp)
				

		A = numpy.matrix(A)
		M,N = A.shape
		Y = numpy.matrix([[1]]*M)
		x = Variable(N)
		objective  = Minimize(sum_entries(square(x)))
		constraints = [Y <= A*x]
		prob = Problem(objective,constraints)
		prob.solve()
		if prob.status == OPTIMAL:
			print 'training completed'
		#print x.value
			self.W = numpy.matrix(x.value)
		
			self.ready = True
		else:
			print 'training not completed'
	def predict(self,X):
		print type(self.W)
		print self.W.shape
		print self.W
		if self.ready == False:
			print 'Warning: The SVM has not been trained'
		Y = []
		for x in X:
			x.append(1)
			if len(x)!= self.M:
				print 'the size of the input is not right'
				return
			
			a = numpy.array(x)*self.W
			if a > 0:
				Y.append([1])
			else:
				Y.append([-1])
		return Y
