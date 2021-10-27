#!/usr/bin/env python3
# -*- coding: utf-8 -*-

rentefot = 2.8 # prosent per år
saldo = 10000

år = 0
while saldo < 20000:
    år += 1
    renter = saldo*rentefot/100
    saldo += renter  
    print(f"Etter {år} år er det {round(saldo)} kr på konto.")

print()
print(f"Det tar {år} år før innskuddet er dobblet.")