#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:51:42 2023

@author: larabibulich
"""
# n = cantidad de discos
# f = pilar de partida (from)
# h = pilar auxiliar (helper)
# t = pilar de destino (target)

def hanoi (n, f, h, t):
    if n==0:
        pass
    else: 
        hanoi(n-1,f,t,h)
        #print ("pillars are f: {}, t: {}, h: {}".format(f,t,h))
        #print ("for disc {}...".format(n))
        #move(f,t)
        print(f"Move disc {n}, from: {f}, to {t}")
        hanoi(n-1, h, f, t)
        
n= int(input("Provide the quantity of disc to return:"))
hanoi(n, f="A", h="B", t="C")
