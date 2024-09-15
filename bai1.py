# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:39:03 2024

@author: Student
"""

n = int(input("Nhập số nguyên dương:"))
giaithua = 1
for i in range (1, n+1):
    giaithua *= i
print(f"Giai thua cua {n}:",n,"!=",giaithua)
    