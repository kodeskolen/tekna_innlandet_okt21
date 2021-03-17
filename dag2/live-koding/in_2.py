# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:42:49 2021

@author: Marie
"""


filnavn = ["bilde.jpg", "program.exe", "bilde2.jpg", "document.docx"]

filtrert_filnavn = []
for navn in filnavn:
    if ".exe" not in navn:
        filtrert_filnavn.append(navn)
        
print(filtrert_filnavn)

ny_liste = [navn for navn in filnavn if ".exe" not in navn]
print(ny_liste)