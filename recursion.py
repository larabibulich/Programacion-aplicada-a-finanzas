#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:25:31 2023

@author: larabibulich
"""
#%% 173 Total the values
#Write a program that reads values from the user until a blank line is entered. Display the total of all of
#the values entered by the user (or 0.0 if the first value entered is a blank line). Complete this task using 
#recursion. Your program may not use any loops.
def vacio ():
    n = input("ingrese un numero: ")
    if n == "":
        return 0
    else: 
        n = int(n) #pasa el numero ingresado a numero entero. 
        return n + vacio() #la funcion devuelve "n" y se vuelve a llamar a la funcion.

total = vacio() 
print ("el numero total es: ", total)    
#%% 174 greatest common divisor
#Write a program that implements Euclid’s algorithm and uses it to determine the greatest common divisor of two 
#integers entered by the user. Test your program with some very large integers. The result will be computed 
#quickly, even for huge numbers consisting of hundreds of digits, because Euclid’s algorithm is extremely 
#efficient.
def MCD(A,B): 
    if B == 0: 
        #porque 10(a) y 0(b) el maximo comun divisor es 10. 
        return A
    else:
        resto = A%B 
        if resto == 0:
            return B
        A = resto
        return MCD (B,A)
#EJEMPLO: 
    #10(a) y 6(B). 10%6=4, 4 pasa a ser A y se vuelve a llamar a la funcion. 
    #b=6, a=4. al volver a inciar la funcion se cambian. a=6, b=4, entonces es 6%4=2. 
    #b=2, a=

a = int(input("ingrese un numero: "))  
b = int(input("ingrese otro numero: "))
print ("el MCD entre",a, "y", b, "es: ", MCD (a,b))

#%% 176 The NATO Phonetic Alphabet
#Write a program that reads a word from the user and then displays its phonetic spelling. For example, if the 
#user enters Hello then the program should output Hotel Echo Lima Lima Oscar. Your program should use a 
#recursive func- tion to perform this task. Do not use a loop anywhere in your solution. Any non-letter 
#characters entered by the user should be ignored.
Abecedario = {"A" : 'Alpha', 'B' : 'Bravo', 'C': 'Charlie', 'D' : 'Delta' , 'E' : 'Echo' ,
            'F' : 'Foxtrot' ,'G' :' Golf', 'H': 'Hotel' ,'I' : 'India', 'J' : 'Juliet' ,
            'S' : 'Sierra ', 'K' : 'Kilo', 'L' : 'Lima' , 'M' :  'Mike',  'N' : 'November',
            'O' : 'Oscar', 'P':  'Papa', 'Q' : 'Quebec' , 'R' : 'Romeo' , 'T' : 'Tango',
            'U' : 'Uniform', 'V' : 'Victor', 'W' : 'Whiskey','X': 'Xray', 'Y':' Yankee',
            'Z' :' Zulu'} #escribo un diccionario. Como vuelvo a correr la funcion, es importante que el
                            #diccionario este afuera de la funcion (es mas eficiente para buscar). 
palabra = input("ingrese una palabra: ")
palabra = palabra.upper() #pasa a ser mayuscula para facilitar el proceso. 

def NATO(Abecedario, palabra):
    if len(palabra) != 1: #!= diferente
       buscar = palabra[1:] #empieza de la segunda letra  (0, 1 ....) hasta el final (:)
       letra = palabra[0] #agarra la primera letra.
       return Abecedario[letra] + " " + NATO(Abecedario,buscar) #busca la letra en el abecedario y vuelve a empezar con lo demas. 
    else: 
       return Abecedario[palabra] #si escriben una letra, devuelve directamente del abecedario. 

NATO(Abecedario, palabra)
#%% 177 
#Create a recursive function that converts a Roman numeral to an integer. Your function should process one or two
#characters at the beginning of the string, and then call itself recursively on all of the unprocessed characters.
#Use an empty string, which has the value 0, for the base case. In addition, write a main program that reads a 
#Roman numeral from the user and displays its value. You can assume that the value entered by the user is valid. 
#Your program does not need to do any error checking.
numeros = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
n_romano = input("ingrese un numero romano: ")
n_romano = n_romano.upper()

def romano (numeros, n_romano):
    if len (n_romano) != 1: 
        buscar = n_romano[1::]
        letra = n_romano[0]
        return numeros[letra] + romano(numeros, buscar)
    else: 
        n= n_romano
        return numeros[n]
x = romano(numeros, n_romano)
print ("el numero es: ", x)
#hay un error con el 19 por ejemplo. devuelvw 21. tengo que mirar el numero siguiente. 
#restar cuando el numero es menor que el que sigue. 
#si el codigo esta bien armado tiene que tener UN SOLO return. 
#%% 177 CON UN SOLO RETURN
numeros = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
n_romano = input("ingrese un numero romano: ")
n_romano = n_romano.upper()
def romano (numeros, n_romano):
    if len (n_romano) != 1: 
        buscar = n_romano[1::]
        letra = n_romano[0]
        salida =  numeros[letra] + romano(numeros, buscar)
    else: 
        n= n_romano
        salida = numeros[n]
    return salida

x = romano(numeros, n_romano)
print ("el numero es: ", x)
#%% 178 Recursive Palindrome
#Write a main program that reads a string from the user and uses your recursive function to determine whether or 
#not it is a palindrome. Then your program should display an appropriate message for the user.
palabra = input("ingrese una palabra: ")
lista = list(palabra)
def palindrome (lista):
    if lista[0]==lista[-1]:
        lista.pop(0)
        lista.pop(-1)
        if len(lista) == 0 or len(lista) == 1:
            print("La palabra es palindrome")
        else:
            palindrome(lista)
    else:
        print("La palabra no es palindrome")

palindrome(lista)


    
    
    
    
    



    
