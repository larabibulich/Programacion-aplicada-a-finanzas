#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:06:00 2023

@author: larabibulich
"""

class FF():
    """ Documentacion que va al __doc__ del objeto
        Poner aqui lo que se quiera explicar en un help.
        Por una cuestion de seguridad, vamos a usar tuplas 
        para garantizar la inmutabilidad del objeto
        """
    def __init__(self,tupla=tuple()):
        self.flujos=tupla
        
    def van(self,tasa, n=0):
        """ Calculo de valor actual neto recursivo
            Inputs: 
                1 - tasa (posicional)
                2 - n posicion en el vector ( default = 0, named argument ). 
                    Sirve para manejar recursivamene las iteraciones 
                    sin alterar la lista del flujo de fondos  
        """
        if len(self.flujos)>0:
            if n==len(self.flujos):
                salida = 0
            else:
                salida = self.flujos[n]+1.0/(1.0+tasa)*self.van(tasa, n=n+1)
        else:
            print('\n',"La tupla de flujo de fondos esta vacia. Se devuelve 0")
            salida = 0
        return salida
    
    def vt(self,tasa,t = 0):
        """ Calculo de valor del flujo de fondos a un tiempo t
            Funciona calculando van y luego llevando a tiempo t correspondiente
            Inputs: 
                1 - tasa (posicional)
                2 - t momento de valuacion ( default = 0, named argument ). 
                    
        """
        return self.van(tasa)*(1.0+tasa)**t
    
#%%
if __name__=='__main__':
    
    a = FF((-80,10,10,10,10,10,10,10,10,100))    

    # dos formas de llamar al help    
    print((a.van).__doc__)
    help(a.vt)        
        
    # Busqueda de TIR...
    for x in range(1,20) : print(x, a.van(x/100.0))   
    
    # van a un valor proximo a la tir...
    print('\n',a.van(0.1330055))
    
    # Valor futuro en t a la tir. 
    # Notar que al no ser la tir exacta, 
    # a 25 periodos hacia el futuro, se aleja del 0.
    # Haria falta una funcion para computar la tir.... :) 
    print('\n', a.vt(0.1330055,25))
    
    
    #test caso FF vacio
    a = FF()
    print('\n',a.van(0.0))
