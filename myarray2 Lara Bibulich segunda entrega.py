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
    
    def ayuda (self):
        if self.by_row:
            lista = self.elems
            return lista
        else:
            total = []
            elems = list(self.elems)
            for n in range(self.c):
                lista = []
                for i in elems:
                    if len(elems)!=0 or len(elems) !=1:
                        lista.append(i[0])
                        i.pop(0)
                total.append(lista)
            print(total)
            return total
          
    def get_pos(self,j,k):
        """funcion devuelve el elemento de la lista elems, segun j(fila) que empieza desde 0 y 
        k(columna) que empieza desde 1"""            
        lista = instancia.ayuda()
        posicion = lista[j][k]
        return posicion
    
    def get_coords(self,m):
        """funcion que toma una posicion M en la lista y devuelve en forma de tupla las 
        coordenadas j,k correspondientes en la matriz"""
        lista = instancia.ayuda()
        for i in range(len(lista)):
            for j in range (len(lista[i])):
                if lista[i][j] == m:
                    return(i,j)
     
    def get_elem(self,j,k): 
         """funcion que devuelve el elemento (j,k) de la matriz"""
         lista = instancia.ayuda()
         return lista[j][k]
    
    def switch (self):
        """devuelve un objeto con la misma matriz pero alterando la lista elems y cambiando el
        valor de verdad de by_row"""
        lista = myarray.ayuda(self)
        for i in lista:
            i.reverse()
        lista.reverse()
        byrow2 = not self.by_row
        print((lista,self.r,self.c,byrow2)) 
        return myarray(lista,self.r,self.c,byrow2)
    
    def get_row(self,j):
        lista = myarray.ayuda(self)
        """funcion que devuelve los elementos de la fila j"""
        lista2 =[]
        lista2.append(lista[j])
        return lista[j]
    
    def get_col(self,k):
        """funcion que devuelve los elementos de la columna k"""
        lista = myarray.ayuda(self)
        lista2= []
        for i in lista:
            lista2.append(i[k])
        return lista2
    
    
    def del_row(self,j):
        """funcion que devuelve un objerto de la clase habiendo eliminado una fila de la matriz"""
        lista = myarray.ayuda(self)
        lista.pop(j)
        return lista
    
    def del_col(self, k):
        """funcion que devuelve un objerto de la clase habiendo eliminado una columna de la matriz"""
        lista = myarray.ayuda(self)
        for i in lista:
            i.pop(k)
        return lista
    
    def swap_rows(self,j,k):
        """devuelven un objeto de la clase con filas (j,k) intercambiadas."""
        lista = myarray.ayuda(self)
        variable = lista[j]
        lista[j]=lista[k]
        lista[k]=variable
        return lista
    
    def swap_cols(self,l,m):
        """devuelven un objeto de la clase con columnas (l,m) intercambiadas."""
        lista = myarray.ayuda(self)
        for i in lista:
            x = i[l]
            i[l]= i[m]
            i[m]=x
        return lista
        
    def scale_row(self,j,x):
        """devuelve al objeto pero con la fila j, multiplicada por k"""
        lista = instancia.ayuda()
        lista[j]=[x*i for i in lista[j]]
        print(lista)
        return myarray(lista,self.r,self.c,self.by_row)
    
    def scale_col(self,j,k):
        """devuelve al objeto pero con la columna j, multiplicada por k"""
        lista = instancia.ayuda()
        x = [list(i) for i in zip(*lista)]
        x[j] = [k*i for i in x[j]]
        lista2 = [list(i) for i in zip(*x)]
        return myarray(lista2,self.r,self.c,self.by_row)
        
    def transpose(self):
        """funcion que devuelve un elemento de la calsse, pero con la matriz transpuesta"""
        lista = instancia.ayuda()
        return [list(i) for i in zip(*lista)]
    
    def flip_rows(self):
        """devuelven una copia del elemento de la clase, pero reflejando especularmente en sus filas"""
        lista = instancia.ayuda()
        lista2 =[]
        for i in reversed(lista):
            lista2.append(i)
        return lista2
    
    def flip_cols(self):
        """devuelven una copia del elemento de la clase, pero reflejando especularmente en sus columnas"""
        lista = instancia.ayuda()
        for i in lista: 
            v = i[0]
            i[0]=i[-1]
            i[-1]=v
        return lista
    
   # def det(self):
        #lista = instancia.ayuda()
        #if self.c == self.r:
         #   if self.c == 2:
          #      det = lista[0][0]*lista[1][1] - lista[0][1]*lista[1][0]
           # elif self.c == 3:

    def add(self,b):
        lista = instancia.ayuda()
        lista2 = []
        if type(b) in [int,float]:
            print("Se suma un escalar")
            for i in lista:
                for n in i:
                    lista2.append(n+b)
            salida = lista2
        elif type(b) == list:
            print("Se suma otra matriz")
            if len(lista) == len(b):
                for i in lista:
                    lista2.extend(i)
                listajunta =[]
                for i in b:
                    listajunta.extend(i)
                salida = [x+y for x,y in zip(lista2,listajunta)]
            else:
                salida = ("No se puede realizar la suma")
        return salida
    
    def sub(self,b):
        lista = instancia.ayuda()
        lista2 = []
        if type(b) in [int,float]:
            print("Se resta un escalar")
            for i in lista:
                for n in i:
                    lista2.append(n-b)
            salida = lista2
        elif type(b) == list:
            print("Se resta otra matriz")
            if len(lista) == len(b):
                for i in lista:
                    lista2.extend(i)
                listajunta =[]
                for i in b:
                    listajunta.extend(i)
                salida = [x-y for x,y in zip(lista2,listajunta)]
            else:
                salida = ("No se puede realizar la resta")
        return salida
    
    def __mul__(self,other):
        aux = map(lambda x: list(map(lambda a: a*other,x)),self.elems)
        return list(aux)
    
    def __rmul__(self,other):
        return self*other
    
    def __matmul__(self,b):
       lista = []
       if self.c == b.r or self.r==b.c:
           for i in range(self.r):
               fila = self.get_row(i)
               for n in range(b.c):
                   columna = b.get_col(n)
                   e = 0
                   for k in range(self.c):
                       e += fila[k] * columna[k]
          
                   lista.append(e)  
       print(lista)
       return lista
       #return myarray(lista2,self.c,self.r,self.by_row)
       
       
    def pow(self,n): #por la matriz propia.
        if self.c==self.r:
            matriz = myarray(self.elems,self.r,self.c,self.by_row)
            resultado = matriz
            for i in range(n-1):
                x = matriz@resultado
                resultado = myarray(x.elems,self.r,self.c,self.by_row)
            return resultado.elems
        
    def swap_cols2(self,j,k):
        i = identidad(self.c,self.c,True)
        ins = i.swap_cols(j,k)
        iden = myarray(ins, self.c, self.c, True)
        a = myarray(self.elems,self.r,self.c,True)
        return (a@iden)
        
    def swap_rows2(self,j,k):
        i = identidad(self.r,self.r,True)
        ins = i.swap_rows(j,k)
        iden = myarray(ins, self.r, self.r, True)
        a = myarray(self.elems,self.r,self.c,True)
        return iden@a
    
    def del_row2(self,j):
        i = identidad(self.r,self.r,True)
        x = i.del_row(j)
        otro = myarray(x,self.r-1,self.r,True)
        a  = myarray(self.elems,self.r,self.c,self.by_row)
        return otro@a
    
    def del_col2(self,k):
        i = identidad(self.c,self.c,True)
        x =i.del_col(k)
        otro = myarray(x,self.c,self.c-1,True)
        a  = myarray(self.elems,self.r,self.c,self.by_row)
        x =  a@otro
        return x
            
class identidad(myarray):
    def __init__(self,r,c,by_row):
        self.r = r
        self.c = c
        self.by_row = by_row
        self.elems =[]
        for i in range(self.r):
            for j in range(self.c):
                if i==j:
                    self.elems.append(1)
                else:
                    self.elems.append(0)  
        m = []
        for i in range(0,len(self.elems),self.r):
            fila = self.elems[i:i+self.r]
            m.append(fila)
        self.elems = m
          
instancia = myarray([[1,2,3],[4,5,6],[7,8,9]],3,3,True)   
#print(instancia.swap_cols(0, 1))       
instancia2 = myarray([[1,2],[1,2]],2,2,True)
   






