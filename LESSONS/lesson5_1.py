import string
import random
def cont_str(s):
    big = 0
    small = 0
    for  sum in s:
     if sum.isupper():
        big += 1
    else:
        small += 1
    if big > small:
         return 1
    elif small > big:  
         return 0
    else:
        return -1    
print()  
            

    


