#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:35:34 2023

@author: larabibulich
"""
#elems = lista conteniendo los elementos de la matriz
#r = indicador de cantidad de filas
#c = indicador de cantidad de columnas
#by_row = tipo boolean, indica la correspondencia entre elementos de la lista y
#elemenos dela matriz. 
class myarray ():
    def __init__ (self,elems,r,c,by_row):
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
    
    def get_pos(self,j,k):
        """funcion devuelve el elemento de la lista elems, segun j(fila) que empieza desde 0 y 
        k(columna) que empieza desde 1"""            
        if self.c*self.r == len(self.elems):
            if self.by_row:
                m = j*self.c + k
            else:
                m = k*self.r + j
            return m
        #j (fila) y k (columna) son las coordenadas de un elemento de la matriz. 
        #las filas empiezan de 0, las columnas de 1. 
    
    def get_coords(self,m):
        """funcion que toma una posicion M en la lista y devuelve en forma de tupla las 
        coordenadas j,k correspondientes en la matriz"""
        if m in self.elems:
            if self.by_row:
                j=m//self.c #division entera
                #5//3 = 1
                k= m % self.c
                #5%3 = 2
                print("get_coords","(",j,",",k,")")
                return j,k
    
    def switch(self):
        """devuelve un objeto con la misma matriz pero alterando la lista elems y cambiando el
        valor de verdad de by_row"""
        lista = self.elems[::-1] #devuelve la matriz al reves
        byrow2 = not self.by_row
        instancia2 = myarray(lista,self.r,self.c,byrow2) # es para combrobar que funciona
        print("switch", instancia2.elems,instancia2.r,instancia2.c,instancia2.by_row) # es para comprobar que funciona
        return myarray(lista,self.r,self.c,byrow2)
    
    def get_row(self,j):  
        """funcion que devuelve los elementos de la fila j"""
        row = []
        if self.by_row:
            for i in range(j*self.c,j*self.c+self.c):
                row.append(self.elems[i])
        else:
            for i in range(self.c):  
                row.append(self.elems[i*self.r+j])
        return row

    def get_col(self,k):
        """funcion que devuelve los elementos de la columna k"""
        column = []
        if self.by_row:
            for i in range(self.r):  
                column.append(self.elems[i*self.c+k])
        else:
            for i in range(k*self.r,k*self.r+self.r): #desde k*2 hasta k*2+2
                column.append(self.elems[i])
        return column
    
    def get_elem(self,j,k):
        """funcion que devuelve el elemento (j,k) de la matriz"""
        if self.by_row:
            elem = self.elems[j*self.c + k]
        else:
            elem = self.elems[k*self.r + j]
        print ("get_elem",elem)
        return elem
   
    def del_row(self,j):
        """funcion que devuelve un objerto de la clase habiendo eliminado una fila de la matriz"""
        fila = self.get_row(j)
        for i in fila:
            self.elems.remove(i)
        print(self.elems)
        return myarray(self.elems,self.r-1,self.c,self.by_row)
     
    def del_col(self,k):
        """funcion que devuelve un objerto de la clase habiendo eliminado una columna de la matriz"""
        fila = self.get_col(k)
        for i in fila:
            self.elems.remove(i)
        print(self.elems)
        return myarray(self.elems,self.r,self.c-1,self.by_row)
                
    def swap_rows(self,j,k):
        """devuelven un objeto de la clase con filas (j,k) intercambiadas."""
        lista = []
        for n in range(1,j):
            lista.extend(self.get_row(n))
        lista.extend(self.get_row(k))
        for n in range(j+1,k):
            lista.extend(self.get_row(n))
        lista.extend(self.get_row(j))
        for n in range(k+1,self.c):
            lista.extend(self.get_row(n))
        return myarray(self.elems,self.r,self.c,self.by_row)
     
    def swap_cols(self,j,k):
        """devuelven un objeto de la clase con las columnas (j,k) intercambiadas."""
        for i in range(self.r):
            columna1 = self.get_pos(i,j)
            columna2 = self.get_pos(i,k)
            variable = self.elems[columna2]
            self.elems[columna2]=self.elems[columna1]
            self.elems[columna1]=variable
        return myarray(self.elems,self.r,self.c,self.by_row)
    
    def scale_row(self,j,k):
        """devuelve al objeto pero con la fila j, multiplicada por k"""
        lista = []
        for n in range(0,j):
            lista.extend(self.get_row(n))
        lista.extend([i*k for i in (self.get_row(j))])
        for n in range(j+1,self.r):
            lista.extend(self.get_row(n))
        return myarray(lista,self.r,self.c,self.by_row)
            
    def scale_col(self,j,k):
        """devuelve al objeto pero con la columna j, multiplicada por k"""
        lista =[]
        for i in range (len(self.elems)):
             if self.get_coords(i)[1] == j:
                lista.append(k*(self.elems[i]))
             else:
                lista.append(self.get_row[i])
        return myarray(lista,self.r,self.c,self.by_row)
    
    def transpose (self):
        """funcion que devuelve un elemento de la calsse, pero con la matriz transpuesta"""
        lista = []
        for i in range (self.c):
            lista.extend(self.get_col(i))
        print(lista)
        return lista
    
    def flip_rows (self):
        """devuelven una copia del elemento de la clase, pero reflejando especularmente en sus filas"""
        lista = []
        for i in range(self.r-1,-1,-1) :
            row = self.get_row(i)
            lista.extend(row)
        return lista
    
    def flip_cols (self):
        """devuelven una copia del elemento de la clase, pero reflejando especularmente en sus columnas"""
        lista = []
        for i in range(self.r-1,-1,-1) :
            columna = self.get_col(i)
            lista.extend(columna)
        return lista



instancia = myarray([1,2,3,4,5,6,7,8,9],3,3,False) #r=2,c=3
#True significa que la matriz es por filas. osea 2 filas:f1=[1,2,3], f2=[4,5,6] y 3 columnas: c1=(1,4),c2=(2,5),c3=(3,6)
#False significa que la matriz es por columnas. osea 2 filas: f1=[1,3,5],f2=[2,4,6] y 3 columnas: c1=[1,2],c2=[3,4],c3=[5,6]


#llamo a las funciones adentro de la clase. 
#instancia.get_pos(0,1)
#instancia.get_coords(3)
#instancia.switch()
#instancia.get_row(1)
#instancia.get_col(1)
#instancia.get_elem(1,2)   
#instancia.del_row(1)                
#instancia.del_col(1)
#instancia.swap_rows(0, 1)
#instancia.swap_cols(0,1)
#instancia.scale_row(1,2)
#instancia.scale_col(1,2) 
#instancia.transpose()
#instancia.flip_rows() 
instancia.flip_cols() 
#dinstancia.scale_col()


 



        
