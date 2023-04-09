import math 
import os 
import random 
import re 
import sys 

def diagnolDifference(arr): # Create the matrix from input arr
    length = len(range(arr))       # lenth of the array 
    left = 0                # define the left diagnol 
    right = 0
    m = 0                   # Dont yet know where this will be used
    n = length -1           # we get the right diagnol where we actually get the lenth of each array - 1
    for i in range(length):
        left += arr[i][i]
        right += arr[m][n]
        n -= 1
        m += 1

    result = left - right
    return result*-1 if result <0 else result


    



m = int(input().strip())
print(diagnolDifference(m))