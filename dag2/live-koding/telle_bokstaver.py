#!/usr/bin/env python3
# -*- coding: utf-8 -*-

bokstaver = 'abcdefghijklmnopqrstuvwxyzæøå'

navn = input("Hva heter du? ")

antall_bokstaver = 0
for tegn in navn:
    if tegn.lower() in bokstaver:
        antall_bokstaver += 1
    
print(f"Det er {antall_bokstaver} bokstaver i navnet ditt.")
