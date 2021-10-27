#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle

personer = ['Andreas', "Monica", "Sindre",
            "Peter", "Silje", "Beate"]

farger = ["rød", "blå", "grønn",
          "svart", "gul", "lilla"]

shuffle(personer)
shuffle(farger)

i = 0
while i < len(personer):
    print(f"Spiller {farger[i]} er {personer[i]}")
    i += 1
    

