import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    res = ""
    if N%2 == 0 and ( N in range( 2, 6 ) or N > 20 ):
        res += "Not "
    res += "Weird"
    print( res )