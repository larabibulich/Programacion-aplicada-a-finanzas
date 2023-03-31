#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:59:22 2023

@author: larabibulich
"""
#el best es el que mejor cumple con la condicion que estoy buscando.
#remaining es el residuo (lo que no seria el mejor caso)
elementos = set(['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 
              'Barium', 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine', 
              'Cadmium', 'Calcium', 'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 
              'Chromium', 'Cobalt', 'Copernicium', 'Copper', 'Curium', 'Darmstadtium', 'Dubnium', 
              'Dysprosium', 'Einsteinium', 'Erbium', 'Europium', 'Fermium', 'Flerovium', 'Fluorine', 
              'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Hassium', 
              'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iridium', 'Iron', 'Krypton', 
              'Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 'Livermorium', 'Lutetium', 'Magnesium', 
              'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury', 'Molybdenum', 'Moscovium', 'Neodymium', 
              'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium', 'Nitrogen', 'Nobelium', 'Oganesson', 
              'Osmium', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 
              'Praseodymium', 'Promethium', 'Protactinium', 'Radium', 'Radon', 'Rhenium', 'Rhodium', 'Roentgenium', 
              'Rubidium', 'Ruthenium', 'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 
              'Silicon', 'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 
              'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 
              'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium'])

def lalista (lista, remaining, best):
    candidates = list(filter(lambda x:x[0] == lista[-1][-1].upper(),remaining))
    if len(candidates)==0: #no hay mas candidates
        if len(lista)>len(best):
            best = lista
            print(len(best))
            print(best)
    else:
        for j in candidates:
            newlist = lista + [j]
            best = lalista(newlist, remaining-set([j]),best)
            
    return best

inicial = input("ingrese elemento inicial: ")
lista = [inicial]
best = lalista(lista,elementos-set(lista),lista)
print(best)
