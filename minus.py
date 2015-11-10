#!/usr/bin/env python
# -*- coding: UTF-8 -*-
sum0=0
sum1=0
for i in range(100,0,-1):
    if i%2==0:
     sum0=sum0-i
    else:
     sum1=sum1-i
print sum0
print sum1
print sum0+sum1
