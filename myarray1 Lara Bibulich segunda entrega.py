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
        """funcion devuelve la posicion del eleem de la lista elems, segun j(fila) y k(columna). """       
        if self.c*self.r == len(self.elems):
            if self.by_row:
                m = j*self.c + k
            else:
                m = k*self.r + j
            return m
    
    def get_coords(self,m):
        """funcion que toma una posicion m en la lista y devuelve en forma de tupla las 
        coordenadas j,k correspondientes en la matriz"""
        if m in self.elems:
            if self.by_row:
                j=m//self.c #division entera
                k= m % self.c
                print("(",j,",",k,")")
                return j,k
    
    def switch(self):
        """Funcion devuelve un objeto con la misma matriz pero alterando la lista elems y cambiando el
        valor de verdad de by_row.
        Se crea la variable llamada lista, para recorrer la matriz al reves. 
        Se crea la variable llamada byrow 2, que devuelve el contrario de by_row (es decir si by_row es True, va a devolver False. 
        """
        lista = self.elems[::-1]
        byrow2 = not self.by_row
        instancia2 = myarray(lista,self.r,self.c,byrow2) # es para combrobar que funciona
        print(instancia2.elems,instancia2.r,instancia2.c,instancia2.by_row) # es para comprobar que funciona
        return myarray(lista,self.r,self.c,byrow2)
    
    def get_row(self,j):  
        """Funcion que devuelve los elementos de la fila j. 
        Se crea una lista vacia, llamada fila, para luego, mediante el append, agregar los elementos de la fila j.
        """
        fila = []
        if self.by_row:
            for i in range(j*self.c,j*self.c+self.c):
                fila.append(self.elems[i])
        else:
            for i in range(self.c):  
                fila.append(self.elems[i*self.r+j])
        return fila

    def get_col(self,k):
        """Funcion que devuelve los elementos de la columna k.
        Se crea una lista vacia, llamada columna, para luego, mediante el append, agregar los elementos de la columna k. """
        columna = []
        if self.by_row:
            for i in range(self.r):  
                columna.append(self.elems[i*self.c+k])
        else:
            for i in range(k*self.r,k*self.r+self.r): #desde k*2 hasta k*2+2
                columna.append(self.elems[i])
        return columna
    
    def get_elem(self,j,k):
        """Funcion que devuelve el elemento (j,k) de la matriz."""
        if self.by_row:
            elem = self.elems[j*self.c + k]
        else:
            elem = self.elems[k*self.r + j]
        print (elem)
        return elem
    
    def del_row(self,j):
        """Funcion que devuelve un objeto de la clase habiendo eliminado una fila de la matriz
        Se crea una lista vacia, llamada lista, para luego ir agregando las filas deseadas, excepto la que se desea borrar."""
        #Corregir el retorno del objeto. 
        lista = []
        if j!=0:
            for i in range(0,j):
                lista.extend(self.get_row(i))
            for i in range(j+1,self.r):
                lista.extend(self.get_row(i))
        else:
            for i in range(1,self.r):
                lista.extend(self.get_row(i))
        return lista
 
    def del_col(self,k):
        """Funcion que devuelve un objerto de la clase habiendo eliminado una columna de la matriz. 
        Se crea una lista vacia en la que se van agregando las columnas, excepto la que se desea eliminar. 
        Como se van agregando las columnas, los elementos quedan desordenados. Por lo tanto, se crea una nueva instancia,
        llamada instancia2, para utilizar la funcion transpose, para crear la matriz transpuesta y devolverla ordenada. """
        lista = []
        if k!=0:
            for i in range(0,k):
                lista.extend(self.get_col(i))
            for i in range(k+1,self.c):
                lista.extend(self.get_col(i))
        else: 
            for i in range(1,self.c):
                lista.extend(self.get_col(i)) 
        instancia2 = myarray(lista,self.c-1,self.r,self.by_row)
        return instancia2.transpose()
        #return myarray(self.elems,self.r,self.c-1,self.by_row)
   
    def swap_rows(self,j,k):
        """Funcion que devuelve un objeto de la clase con filas (j,k) intercambiadas.
        Se crea una lista vacia para agregar todas las filas, y agregar las filas intercambiadas en sus nuevos lugares."""
        lista = []
        for n in range(0,j):
            lista.extend(self.get_row(n))
        lista.extend(self.get_row(k))
        for n in range(j+1,k):
            lista.extend(self.get_row(n))
        lista.extend(self.get_row(j))
        if k == self.r-1:
            return lista
        else:
            for n in range(k+1,self.c):
                lista.extend(self.get_row(n))
        return lista
        #return myarray(self.elems,self.r,self.c,self.by_row)

    def swap_cols(self,j,k):
        """Funcion que devuelve un objeto de la clase con las columnas (j,k) intercambiadas.
        Se crea una lista de los elementos de la clase (elems) para cambiar sus lugares."""
        lista = list(self.elems)
        for i in range(self.r):
            columna1 = self.get_pos(i,j)
            columna2 = self.get_pos(i,k)
            variable = lista[columna2]
            lista[columna2]=lista[columna1]
            lista[columna1]=variable
        print(lista)
        #return myarray(self.elems,self.r,self.c,self.by_row)
        return lista
    
    def scale_row(self,j,k):
        """Fucnion que devuelve al objeto pero con la fila j, multiplicada por k.
        Se crea una lista vacia para agrefar las filas, y la fila cambiada."""
        lista = []
        for n in range(0,j):
            lista.extend(self.get_row(n))
        lista.extend([i*k for i in (self.get_row(j))])
        for n in range(j+1,self.r):
            lista.extend(self.get_row(n))
        print(lista)
        return myarray(lista,self.r,self.c,self.by_row)
           
    def scale_col(self,j,k):
        """Devuelve al objeto pero con la columna j, multiplicada por k.
        Se crea una lista con los elementos de la clase, para luego modificar la misma.
        Se crea la variable llamada columna para encontrar la columna que se desea modificar.
        """
        lista = list(self.elems)
        columna = self.get_col(j)
        for i,n in enumerate(columna):
            pos = self.get_pos(i,j)
            lista[pos] = n*k
        print(lista)
        return myarray(lista,self.r,self.c,self.by_row)
        
    def transpose (self):
        """Funcion que devuelve un elemento de la clase, pero con la matriz transpuesta.
        Se crea una lista vacia, para que mediante el for i se vaya agregando las respectivas columnas en filas."""
        lista = []
        for i in range (self.c):
            lista.extend(self.get_col(i))
        print(lista)
        return lista
    
    def flip_rows (self):
        """Fucnion que devuelven una copia del elemento de la clase, pero reflejando especularmente en sus filas.
        Se crea una lista vacia para agregar esto."""
        lista = []
        for i in range(self.r-1,-1,-1) :
            row = self.get_row(i)
            lista.extend(row)
        print(lista)
        return lista
    
    def flip_cols (self):
        """Devuelven una copia del elemento de la clase, pero reflejando especularmente en sus columnas.
        Se crea una lista vacia para agregar esto."""
        lista = []
        for i in range(self.r-1,-1,-1) :
            columna = self.get_col(i)
            lista.extend(columna)
        print(lista)
        return lista
        
    def add (self,b):
        """Funcion que realiza una suma entre matrices, o una suma entre la matriz y un escalar.
        En caso de que se ingrese un escalar para realizar la suma, se crea una lista vacia para ir agregando los resultados.
        En caso de que se ingrese otra matriz, y la matriz sea del mismo tamaño, se realiza la suma, elemento por elemento. 
        """
        lista = []
        if type(b) in [int,float]:
            print("Se suma un escalar")
            for i in self.elems:
                lista.append(i+b)
            salida = lista
        elif type(b) == list:
            print("Se suma otra matriz")
            if len(self.elems) == len(b):
                salida = [x+y for x,y in zip(self.elems,b)]
            else:
                salida = ("No se puede realizar la suma")
        return salida
    
    def sub(self,b):
        """Funcion que realiza una resta entre matrices, o una resta entre la matriz y un escalar.
        En caso de que se ingrese un escalar para realizar la resta, se crea una lista vacia para ir agregando los resultados.
        En caso de que se ingrese otra matriz, y la matriz sea del mismo tamaño, se realiza la resta, elemento por elemento. 
        """
        lista = []
        if type(b) in [int,float]:
            print("Se resta un escalar")
            for i in self.elems:
                lista.append(i-b)
            salida = lista
        elif type(b) == list:
            print("Se resta otra matriz")
            if len(self.elems) == len(b):
                salida = [x-y for x,y in zip(self.elems,b)]
            else:
                salida = ("No se puede realizar la resta")
        return salida
        
    def __mul__(self,b):
        lista = []
        if (isinstance(b,int)):
            [lista.append(i*b) for i in self.elems]
        return lista
         
    def __rmul__(self,b):
        lista = [] 
        if (isinstance(b,int)):
            [lista.append(i*b) for i in self.elems]
        return myarray(lista,self.r,self.c,self.by_row)
   
    def __matmul__ (self,b):
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
            return lista 

    def lrpod(self,b):
        """Funcion que multiplica la matriz por izquierda, usando matmul"""
        return (self@b)
    
    def rprod(self,b):
        """Funcion que multiplica la matriz por derecha, usando matmul"""
        return(b@self)
    
    def pow(self,n): 
        """Funcion que realiza una potencia para la matriz dada. Para realizar la multiplicacion, la cantidad de 
        columnas tiene que ser igual a la cantidad de filas. Se crea la isntancia matriz y resultado, siendo la misma,
        par aluego modificar la isntancia resultado, multiplicando a la matriz por si misma e ir guardando el resultado."""
        if self.c==self.r:
            matriz = myarray(self.elems,self.r,self.c,True)
            resultado = myarray(self.elems,self.r,self.c,True) 
            for i in range(n-1):
                x = matriz@resultado
                resultado = myarray(x,self.r,self.c,True)
            return resultado.elems
    
    def swap_cols2(self,j,k):
        """Funcion que devuelve un objeto de la clase con las columnas (j,k) intercambiadas.
        Esto se realiza mediante la mutliplicacion de una identidad. A la identidad se le cambian las columnas que se desean cambiar, 
        para luego multiplicarla por la matriz. De esta manera se consigue la matriz con las columnas intercambiadas.
        Se crea la variable llamada i, para conseguir la identidad.
        Se crea la variable i_cambiada para cambiar las columnas deseadas.
        Se crea la instancia ident, con la identidad con las columnas cambiadas.
        Se crea la instancaia matriz, la que se desea modificar.
        Se multiplica la matriz por la identidad, mediante ___matmul___ para obtener el resultado deseado."""
        i = identidad(self.c,self.c,True)
        i_cambiada = i.swap_cols(j,k)
        ident = myarray(i_cambiada, self.c, self.c, True)
        matriz = myarray(self.elems,self.r,self.c,True)
        return (matriz@ident)
    
    def swap_rows2(self,j,k):
        """Funcion que devuelve un objeto de la clase con las filas (j,k) intercambiadas.
        Esto se realiza mediante la mutliplicacion de una identidad. A la identidad se le cambian las filas que se desean cambiar, 
        para luego multiplicarla por la matriz. De esta manera se consigue la matriz con las filas intercambiadas.
        Se crea la variable llamada i, para conseguir la identidad.
        Se crea la variable i_cambiada para cambiar las filas deseadas.
        Se crea la instancia ident, con la identidad con las filas cambiadas.
        Se crea la instancaia matriz, la que se desea modificar.
        Se multiplica la identidad por la matriz, mediante ___matmul___ para obtener el resultado deseado."""
        i = identidad(self.r,self.r,True)
        i_cambiada = i.swap_rows(j,k)
        ident= myarray(i_cambiada, self.r, self.r, True)
        matriz = myarray(self.elems,self.r,self.c,True)
        return (ident@matriz)
    
    def del_row2(self,j):
        """Funcion que devuelve un objerto de la clase habiendo eliminado una fila de la matriz.
        Esto se realiza mediante la mutliplicacion de una identidad. A la identidad se le elimina la fila que se desea, 
        para luego multiplicarla por la matriz. De esta manera se consigue la matriz con la fila eliminada.
        Se crea la variable llamada i, para conseguir la identidad.
        Se crea la variable i_cambiada para eliminar la fila deseada.
        Se crea la instancia ident, con la identidad la fila eliminada. 
        Se crea la instancaia matriz, la que se desea modificar.
        Se multiplica la identidad por la matriz, mediante ___matmul___ para obtener el resultado deseado.
        """
        i = identidad(self.r,self.r,True)
        i_cambiada = i.del_row(j)
        ident = myarray(i_cambiada,self.r-1,self.r,True)
        matriz  = myarray(self.elems,self.r,self.c,self.by_row)
        print(ident@matriz)
        return ident@matriz
         
    def del_col2(self,k):
        """Funcion que devuelve un objerto de la clase habiendo eliminado una columna de la matriz.
        Esto se realiza mediante la mutliplicacion de una identidad. A la identidad se le elimina la columna que se desea, 
        para luego multiplicarla por la matriz. De esta manera se consigue la matriz con la columna eliminada.
        Se crea la variable llamada i, para conseguir la identidad.
        Se crea la variable i_cambiada para eliminar la columna deseada.
        Se crea la instancia ident, con la identidad la columna eliminada. 
        Se crea la instancaia matriz, la que se desea modificar.
        Se multiplica la identidad por la matriz, mediante ___matmul___ para obtener el resultado deseado.
        """
        i = identidad(self.c,self.c,True)
        i_cambiada =i.del_col(0)
        ident = myarray(i_cambiada,self.c,self.c-1,True)
        matriz  = myarray(self.elems,self.r,self.c,self.by_row)
        return matriz@ident
       
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
                    
instancia = myarray([1,2,3,4,5,6,7,8,9],3,3,True) #r=2,c=3
iiii = myarray([1,2,3,4,5,6,],2,3,True)
#True significa que la matriz es por filas. osea 2 filas:f1=[1,2,3], f2=[4,5,6] y 3 columnas: c1=(1,4),c2=(2,5),c3=(3,6)
#False significa que la matriz es por columnas. osea 2 filas: f1=[1,3,5],f2=[2,4,6] y 3 columnas: c1=[1,2],c2=[3,4],c3=[5,6]
instancia3 = myarray([2,2,2,2,2,2],3,2,True)
identidaddd = myarray([1,0,0,0,1,0,0,0,1],3,3,True)

#Imprimo las funciones para probar que funcionan todas. (En todas las funciones hay un "print" para 
#observar en la consola el resultado deseado. Si se desea, se puede eliminar.)
print("Get_pos")
instancia.get_pos(0,0)
print("Get_coords")
instancia.get_coords(1)
print("Switch")
instancia.switch()
print("Get_row")
instancia.get_row(0) 
print("Get_col")
instancia.get_col(0)
print("Get_elem")
instancia.get_elem(0,0)
print("Del_row")
instancia.del_row(0)
print("Del_col")
instancia.del_col(0)
print("Swap_cols")
instancia.swap_cols(0,1)
print("Swap_rows")
instancia.swap_rows(0,1)
print("Sclale_row")
instancia.scale_row(0,2)
print("Scale_col")
instancia.scale_col(0,2)
print("Transpose")
instancia.transpose()
print("Flip_rows")
instancia.flip_rows()
print("Flip_cols")
instancia.flip_cols()
#Aclaracion: si se quiere visualizar get_col,get_row,del_col,del_row agregar print en sus funciones,
#ya que si se agrega ahora se imprime varias veces porque estas funciones se usan en varias funciones. 

#Multiplicacion por derecha e izquierda:
instancia.lrpod(instancia3)
instancia.rprod(instancia3)

#Probar que funciona la identidad:
print("Identidad",identidad(2,2,True))

#Multiplicando por identidad:
print("Swap_cols2")
instancia.swap_cols2(0,1)
print("Swap_rows2")
instancia.swap_rows2(0,1)
print("Del_row2")
instancia.del_row2(0)
print("Del_col2")
instancia.del_col2(0)





