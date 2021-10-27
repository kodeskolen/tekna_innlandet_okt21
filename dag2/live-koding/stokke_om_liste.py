#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle

personer = ["Andreas", "Monica", "Sindre",
            "Peter", "Silje", "Beate"]

# Stokke om på lista
shuffle(personer)

print("Tilfeldige rekkefølge:")
for navn in personer:
    print(navn)
