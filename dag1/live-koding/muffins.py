# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:45:23 2021

@author: Marie
"""
from math import ceil

n = 10
print(f"For {n} antall muffins:")
print(f"- {n*150/12} g smør")
print(f"- {n*2/12:.2f} dl sukker")
print(f"- {ceil(n*3/12)} stk egg")
print(f"- {n*5/12:.1f} dl hvetemel")
print(f"- {n/12:.2f} ss bakepulver")