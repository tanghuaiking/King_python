# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:31:24 2019

@author: king
"""
import numpy as np

a=np.arange(13)
#array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])

n=np.arange(0,30,2)
# output is array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

n=n.reshape(3,5)
#output is array([[ 0,  2,  4,  6,  8],
#                [10, 12, 14, 16, 18],
#                [20, 22, 24, 26, 28]])

o=np.linspace(0,4,9)
#output is array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. ])

o.resize(3,3)
#array([[0. , 0.5, 1. ],
#       [1.5, 2. , 2.5],
#       [3. , 3.5, 4. ]])

np.ones((3,2))
#array([[1., 1.],
#       [1., 1.],
#       [1., 1.]])

np.zeros((3,2))
#array([[0., 0.],
#       [0., 0.],
#       [0., 0.]])

np.eye(3)
#array([[1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.]])

#################comput
x=np.array([4,5,6])
y=np.array([4,5,6])
#array([4, 5, 6])

np.diag(y)
#array([[4, 0, 0],
#       [0, 5, 0],
#       [0, 0, 6]])

np.array([1,2,3]*3)
#array([1, 2, 3, 1, 2, 3, 1, 2, 3])

np.repeat([1,2,3],3)
#array([1, 1, 1, 2, 2, 2, 3, 3, 3])

p=np.ones([2,3],int)
#array([[1, 1, 1],
#       [1, 1, 1]])

np.vstack([p,2*p])
#array([[1, 1, 1],
#       [1, 1, 1],
#       [2, 2, 2],
#       [2, 2, 2]])

np.hstack([p,2*p])
#array([[1, 1, 1, 2, 2, 2],
#       [1, 1, 1, 2, 2, 2]])
###################################
#x=array([4, 5, 6])
x+y
#array([ 8, 10, 12])

x.dot(y)
#77

z=np.array([y,y**2])
#array([[ 4,  5,  6],
#       [16, 25, 36]])

z.shape
# (2, 3)

z.T
#array([[ 4, 16],
#       [ 5, 25],
#       [ 6, 36]])

z.T.shape
# (2, 3)

z.dtype
#dtype('int32')

z=z.astype('f')
#array([[ 4.,  5.,  6.],
#       [16., 25., 36.]], dtype=float32)

z.dtype
# dtype('float32')

a=np.array([-2,-3,1,2,3,3,3,3])
a.sum()
a.max()
a.mean()
a.std()
a.argmax()

a=np.array([[-2,-3,1],[1,2,3]])
a.sum()
a.max()
a.mean()
a.std()
a.argmax()
########### index
a=np.arange(13)**2
a
a[0]
a[1:5]
a[-4:]
a[-5::-2]


######  output matrix
import numpy as np
test=np.random.randint(0,10,(4,3))

for row in test:
    print(row)
    
for i in range(len(test)):
    print(test[i])    
    
for i ,row in enumerate(test):
    print('row',i,'is',row)
test2=test**2

for i,j in zip(test,test2):
    print(i,'+',j,'=',i+j)
##############################    