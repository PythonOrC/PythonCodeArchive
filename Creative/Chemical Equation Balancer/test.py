'''
a = 'a'
b = ''
b += a

print(b)
'''
'''
section = 'Ha12OC'
new = True
subscript = ''
import re

splitted = re.findall('\d+|\D+', section)


print(splitted)
for i in range(len(section)):
    if section[i].isnumeric():
        if new == False:
            subscript += section[i]
        else:
            subscript = ''
            subscript += section[i]
            new = False
        
    else:
        if subscript:
            print(subscript)
        new = True
'''
'''

h_list = [2,0,2]
o_list = [0,2,1]

import math
import sympy as sp
import re
import numpy as np
from fractions import Fraction

a = [
    [1,0,-3,0], 
    [2,4,-8,-1], 
    [2,3,0,-2],
    [0,1,-2,0]
]
a = sp.Matrix(a)
print(a.nullspace())
ans = list(a.nullspace()[0])
multiple = sp.lcm([i.q for i in ans])
solution = [num*multiple for num in ans]
factor = sp.gcd([i for i in solution])
solution = [num*multiple for num in ans]
print(solution)

# H + O2 --> H2O
'''
for i in range(0,10,2):
    print(i)
