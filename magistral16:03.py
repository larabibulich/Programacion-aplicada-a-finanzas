#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:35:05 2023

@author: larabibulich
"""

class a():
    x=23
class b(a):
    y = 30
    
z=b() #z es una instancia de la clase b. 

#print(z.x)
print(z._dict_['x']  ) 
#%%
class a:
    x = 23
class b:
    y = 40
    def __init__(self,value):
        self.z = value
w = b(50)
v = b(45)
print(w.z)   
print(v.z)