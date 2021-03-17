# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:52:50 2021

@author: Marie
"""

handleliste = ["melk", "egg", "mel", "sukker"]

prisliste = [28, 26, 13, 22.5]

mengder = [1, 2, 1, 4]

for vare, pris, mengde in zip(handleliste, prisliste, mengder):
    print(f"Vare: {vare:6}, Pris: {pris*mengde:.2f} kr")
    
if "salt" in handleliste:
    print("det er med")