# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:33:08 2016

@author: king
"""


f=open(r'love.txt','w')
f.write('I love you 紫微!\n')
f.write('You have my heart!\n')
f.close()

#
f=open(r'love.txt','r')
p1=f.read()
print(p1)
