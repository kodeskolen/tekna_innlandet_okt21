# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:35:32 2021

@author: Marie
"""

tekst = input("Skriv en beskjed: ")
tekst = tekst.lower()
print(tekst)

if "spam" in tekst:
    print("Spam detektert!")
else:
    print("Ingen spam!")