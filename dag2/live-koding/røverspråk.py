#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Røverspråkets regler:
    For hver konsonant i en beskjed, 
    legg til en 'o' og gjenta konsonanten

Eksempel:
    KATT -> KOKATOTTOT

Steg:
    1.) Gå igjennom beskjed tegn for tegn - LØST
    2.) Bestemme om det er konsonant eller vokal - LØST
    3.) For vokaler, gjør ingenting - LØST
    4.) For konsonanter, legg til "xox" - LØST

Flisespikking: Pass på store bokstaver med .lower() - LØST
"""

vokaler = 'aeiouyæøå'
konsonanter = 'bcdfghjklmnpqrstvwxz'

beskjed = input("Beskjed: ")
hemmelig_beskjed = ""

for tegn in beskjed:
    if tegn.lower() in vokaler:
        hemmelig_beskjed += tegn
    elif tegn.lower() in konsonanter:
        hemmelig_beskjed += f"{tegn}o{tegn.lower()}"
    else:
        hemmelig_beskjed += tegn
        
print(hemmelig_beskjed)

