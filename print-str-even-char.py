#!/usr/bin/env python3

str = input("Enter the string: ")
strlen = len(str)
print(strlen)
i=1
while i <= strlen:
  if i%2 == 0:
     print (str[i-1])
     i = i + 1
  else:
     i = i + 1 
