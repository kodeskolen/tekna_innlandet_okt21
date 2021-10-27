#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle

personer = ["Andreas", "Beate", "Cecilie",
            "Daniel", "Erik", "Finn", "Emilie"]

farger = ["rød", "gul", "grønn", "sort",
          "blå", "lilla", "turkis"]

shuffle(personer)
shuffle(farger)

for navn, farge in zip(personer, farger):
    print(f"Spiller {navn} får de {farge} brikkene.")
    
    