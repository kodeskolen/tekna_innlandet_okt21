#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filer = ["bilde.jpg", "program.exe", 
           "bilde2.jpg", "document.docx"]

bildefiler = []

for filnavn in filer:
    if ".jpg" in filnavn or ".png" in filnavn:
        bildefiler.append(filnavn)       
        
print(bildefiler)
        