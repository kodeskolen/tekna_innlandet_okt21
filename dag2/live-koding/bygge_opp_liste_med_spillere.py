#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
I dette programmet begynner vi med en tom liste og 
legger til én og én spiller. Til slutt skriver
vi ut spillerene i en tilfeldig rekkefølge

Notis: .lower() oversetter en tekststreng til små bokstaver
"""

# Lag en helt tom liste
spillere = []

# Fortsatt å spørre om navn til brukeren skriver "slutt"
navn = input("Skriv inn navn på spiller: ")
while navn.lower() != 'slutt':
    spillere.append(navn)
    navn = input("Skriv inn navn på spiller (Skriv 'slutt' for å avslutte): ")
    
# Stokk om på lista
from random import shuffle
shuffle(spillere)

print(f"Spillerene i tilfeldig rekkefølge:")
for navn in spillere:
    print(navn)