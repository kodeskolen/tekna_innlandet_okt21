# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:49:46 2021

@author: Marie
"""


"""
katt -> kokatottot
Gå igjennom alle bokstavene i et ord- LØST
Dersom det er en konsonant, si konsonant+o+konsonant - LØST
Dersom det er en vokal, bare si vokalen - LØST
"""

tekst = input("Skriv noe: ")
konsonanter = "bcdfghjklmnpqrstvwxz"

for bokstav in tekst.lower():
    if bokstav in konsonanter:
        print(bokstav+"o"+bokstav, end="")
    else:
        print(bokstav, end="")
        
        
        
        