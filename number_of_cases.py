# @Author YoungMinKim

import math
def permutation_len(n,r):
    return math.factorial(n)/math.factorial(r)
def combinations_len(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
