#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:49:01 2023

@author: larabibulich
"""

fv = 206
rate = 0.025
periods =  10

pv = fv/(1+rate)**periods

print("the present value was {:2.2f}".format(round(pv,2)))
[print(f"the present value at year {i} is {pv*(1+rate)**i}")for i in range (10+1)]