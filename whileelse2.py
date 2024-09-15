# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:34:25 2024

@author: Student
"""

count = 0
n=int (input ("Nhập vào số lần cần lặp: "))
while (count < n): 
    print ("Lần lập thứ:", count + 1, "tBiến đếm:", count)
    count = count + 1
else:
    print("\nThực hiện lệnh trong else, do:",
          "\ncount = ", count, "\nn = ", n, 
          "\nbool (count < n) = ", bool (count<n))