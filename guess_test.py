# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:17:16 2016
test input if while
@author: king
"""
from random import randint
x=randint(0,10)
go='y'
while(go=='y'):
  print ('please guass 1~10:')
  digit=int(input())
  if digit==x:
     print('bingo')
     break
  elif digit>x:
      print ('too large' )
  else:
      print ('too small' )
  print('continue,input y')
