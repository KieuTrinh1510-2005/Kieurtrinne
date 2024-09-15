# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:32:58 2024

@author: Student
"""

import random
N = int(input("Nhap so luong phan tu duoc chon:"))
ds = [random.randrange(20,30) for i in range(N)]
print("So ngau nhien la:",ds)
bp = [round(random.uniform(18,99),2 ) for i in range(N)]
print("Gia tri binh phuong cua so thuc:",bp)
