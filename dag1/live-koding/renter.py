# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:59:25 2021

@author: Marie
"""


rente = 2.8
vekstfaktor = 1 + rente/100
innskudd = 1000
pengemengde = innskudd

år = 0

while pengemengde < 2*innskudd:
    print(f"Etter {år:2d} år: {pengemengde:.2f} kr")
    år += 1
    pengemengde *= vekstfaktor
    
print(f"Det tok {år} år å dobble pengene")

