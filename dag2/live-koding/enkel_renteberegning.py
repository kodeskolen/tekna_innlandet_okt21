#!/usr/bin/env python3
# -*- coding: utf-8 -*-

rentefot = 2.8 # prosent per år
saldo = 10000

renter = saldo*rentefot/100

print(f"Etter ett år har vi tjent {renter} kr i renter.")

saldo += renter

print(f"Saldo blir da {saldo} kr.")