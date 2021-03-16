# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:16:04 2021

@author: Marie
"""

"""
Vi "tenker" på et tall mellom 0 og 100
Spilleren gjetter på et tall
Dersom gjettet er riktig så er spillet over og spilleren vant
Dersom gjettet er feil så får spilleren beskjed om det for lite eller for stort
Så får spilleren gjette på nytt
Spilleren har et maks antall gjett
"""
from random import randint

riktig_tall = randint(0, 100)
maks_forsøk = 10

gjett = int(input("Gjett et tall mellom 0 og 100: "))
forsøk = 1

while gjett != riktig_tall and forsøk < maks_forsøk:
    print(f"Du har brukt {forsøk} forsøk")
    if gjett < riktig_tall:
        print("For lavt!")
    else:
        print("For høyt!")
    gjett = int(input("Gjett igjen: "))
    forsøk += 1

if gjett == riktig_tall:
    print("Det var riktig!")
    print("Gratulerer :D")
else:
    print(f"Du har brukt opp dine {maks_forsøk} forsøk")
    print("game over :(")



