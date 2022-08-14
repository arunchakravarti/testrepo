# from array import *
# # user input function
# arr = array('i',[])
# n = int(input("enter the length of array"))
# for i in range (n):
#     val = int(input("enter the values"))
#     arr.append(val)
# print(arr)
# #getting index value by manually
# s = int(input("enter the value to get index"))
# coun = 0
# for i in arr:
#     if i == s:
#         print(coun)
#         break
#     coun +=1
# #getting index by ysing function
# print(arr.index(s))


import numpy as np
a = []
n = int(input("ente rthe range"))
for i in range(n):
    val = int(input("ente rthe values"))
    a.append(val)
arr = np.array(a,float)  # float can change all the int value to float
print(arr)