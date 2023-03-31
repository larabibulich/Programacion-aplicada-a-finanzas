#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:36:09 2023

@author: larabibulich
"""
#%%
class ff():
    def __init__(self, flujos, tasa): 
        self.flujos = flujos #Instancia de la clase, lo que puse en los parametros me lo guarda en la instancia. 
        self.tasa = tasa  #Intancia de la clase 
    def van (self) : #
        flujo = self.flujos 
        tasa = self.tasa 
        #deberia escribir toda la funcin del van
    def vf (self,tiempo) : #
        f = self.flujos 
        t = self.tasa 
        #deberia escribir toda la funcin del van
        
x = ff(flujo,tasa) #me tira error no se pq
w = x.van()
#%%
class ff():
    def __init__(self, flujos, tasa): 
        self.flujos = flujos 
        self.tasa = tasa
    def valor_actual(self,tir,n=-1):#los dos elementops que estan son self y tir. entonces puedo incluir self.flujos
        self.tasa=tir
        if n==len(self.flujos): #n es un valor default que se agrego. 
            salida = 0 #cuando termina la lista, afuera. 
        else:
            salida = self.flujos[n]+1/(1+tir)*self.valor_actual(tir,n+1)
        salida = self.valor_actual(tir,self.flujos)
        return salida
        
    #logramos achicar lo de aca abajo en lo de arriba (parte del else):
        #elemento_a_modificar= self.flujos[-1]
        #numero_de_periodos=len(self.flujos)
        #elemento_a_modificar=elemento_a_modificar/((1+tir)**(numero_de_periodos-1))
        #self.flujos=self.flujos[:-1]
        #salida = elemento_a_modificar+valor_actual(tir, self.flujos)
