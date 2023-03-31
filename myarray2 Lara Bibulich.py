#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:05:44 2023

@author: larabibulich
"""

class myarray ():
    def __init__ (self,elems,r,c,by_row):
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
            
    def get_pos(self,j,k):
        """funcion devuelve el elemento de la lista elems, segun j(fila) que empieza desde 0 y 
        k(columna) que empieza desde 1"""            
        posicion = self.elems[j][k]
        return posicion
    
    def get_coords(self,m):
        """funcion que toma una posicion M en la lista y devuelve en forma de tupla las 
        coordenadas j,k correspondientes en la matriz"""
        for i in range(len(self.elems)):
            for j in range (len(self.elems[i])):
                if self.elems[i][j] == m:
                    return(i,j)
    
    def switch (self):
        """devuelve un objeto con la misma matriz pero alterando la lista elems y cambiando el
        valor de verdad de by_row"""
        for i in self.elems:
            i.reverse()
        self.elems.reverse()
        byrow2 = not self.by_row
        return myarray(self.elems,self.r,self.c,byrow2)
    
    def get_row(self,j):
        """funcion que devuelve los elementos de la fila j"""
        lista =[]
        if self.by_row:
            lista.append(self.elems[j])
        else:
            for i in range(self.r):
                lista.append(self.elems[i][j])
        return lista
   
    def get_col(self,k):
        """funcion que devuelve los elementos de la columna k"""
        lista =[]
        if self.by_row:
            for i in range(self.r):
                lista.append(self.elems[i][k]) #me da mal.
        else:
            lista.append( self.elems[k])
        return lista
    
    def get_elem(self,j,k): 
        """funcion que devuelve el elemento (j,k) de la matriz"""
        return self.elems[j][k]
    
    def del_row(self,j):
        """funcion que devuelve un objerto de la clase habiendo eliminado una fila de la matriz"""
        if self.by_row:
            self.elems.pop(j)
            return  (self.elems)
    
    def del_col(self, k):
        """funcion que devuelve un objerto de la clase habiendo eliminado una columna de la matriz"""
        self.elems.pop(k)
        salida = (self.elems)
        return salida
    
    def swap_rows(self,j,k):
        """devuelven un objeto de la clase con filas (j,k) intercambiadas."""
        variable = self.elems[j]
        self.elems[j]=self.elems[k]
        self.elems[k]=variable
        return myarray(self.elems,self.r,self.c,self.by_row)
        
    def transpose(self):
        """funcion que devuelve un elemento de la calsse, pero con la matriz transpuesta"""
        return[list(i)for i in zip(*self.elems)]
    
    def scale_row(self,j,x):
        """devuelve al objeto pero con la fila j, multiplicada por k"""
        lista =  [list(i) for i in self.elems]
        lista[j]=[x*i for i in self.elems[j]]
        return myarray(lista,self.r,self.c,self.by_row)
                       
    def scale_col(self,k,y):
        """devuelve al objeto pero con la columna j, multiplicada por k"""
        lista = [list(i) for i in self.elems]
        for i in range(self.c):
            lista[i][k] *= y
        return myarray(lista,self.r,self.c,self,self.by_row)
    
    def flip_rows(self):
        """devuelven una copia del elemento de la clase, pero reflejando especularmente en sus filas"""
        lista =[]
        for i in reversed(self.elems):
            lista.append(i)
        return (lista)
    
    def flip_cols(self):
        """devuelven una copia del elemento de la clase, pero reflejando especularmente en sus columnas"""
        print(self.elems)
        for i in self.elems: 
            v = i[0]
            i[0]=i[-1]
            i[-1]=v
        print(self.elems)
        
    
instancia = myarray([[1,2,3],[4,5,6]],2,2,True)




    



    




