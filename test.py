from numpy import random

from svm import svm


# synthese Data
N_train = 100
X = []
Y = []

for k in xrange(N_train):
	if random.randn() < 0:
		X.append([-1+random.randn()*0.5,-1+random.randn()*0.5])
		Y.append([-1])
	else:
		X.append([1+random.randn()*0.5,1+random.randn()*0.5])
		Y.append([1])
N_test = 100
X_test = []
Y_test = []

for k in xrange(N_test):
	if random.randn() < 0:
		X_test.append([-1+random.randn()*0.5,-1+random.randn()*0.5])
		Y_test.append([-1])
	else:
		X_test.append([1+random.randn()*0.5,1*random.randn()*0.5])
		Y_test.append([1])

s = svm(2+1)

s.train(X,Y)

Y_pre = s.predict(X_test)

for k in xrange(len(Y_pre)):
	print Y_test[k][0]-Y_pre[k][0]






