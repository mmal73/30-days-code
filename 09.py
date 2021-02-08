import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if( n > 1 ):
        return n * factorial(n - 1)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') #environment variable with name OUTPUT_PATH

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()