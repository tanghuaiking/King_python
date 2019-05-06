#!/usr/bin/python
from sympy import *

###计算极限
x = Symbol('x')
a=limit(sin(x)/x, x, 0)
print(a)
###计算积分
b=integrate(1/x, x)
print(b)
