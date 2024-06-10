#!/usr/bin/env python3

prevnum=0
curnum=0

range = input("Enter Range: ")
i=1
while i <= 10:
   print ( prevnum + curnum)
   prevnum = curnum
   curnum = curnum + 1
   i = i + 1

 
