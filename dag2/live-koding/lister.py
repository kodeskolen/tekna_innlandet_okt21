# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:40:28 2021

@author: Marie
"""
    
navn1 = "Marie"
navn2 = "Robert"
navn3 = "Jorunn"

kule_kodere = ["Marie", "Robert", "Jorunn", "bastian", "Johanne"]

lengde = len(kule_kodere)

print(kule_kodere[-2])
kule_kodere[3] = "Bastian"
print(kule_kodere)
kule_kodere.append("Johan Emil")
print(kule_kodere)
kule_kodere.insert(3, "Eina")
print(kule_kodere)
kule_kodere = kule_kodere + ["Eli", "Åshild"]
print(kule_kodere)
kule_kodere.sort()
print(kule_kodere)
print(kule_kodere[0:9:2])
print(kule_kodere[-1])





