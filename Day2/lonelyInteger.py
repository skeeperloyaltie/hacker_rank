##  Exclusive OR 
"""
    its represented by the '^' sign
    basically the operator does
    
"""

def lonelyInteger(a): # takes a integer list 
    x = 0
    for i in a:
        x ^= i

    return x
    



a = [3,3,5,5,5,9,6,7,7,7, 6]
# a = [1,1]
# a = [1,1,2]
print(lonelyInteger(a))