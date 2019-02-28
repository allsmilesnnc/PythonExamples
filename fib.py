# This is Python 2
import sys
import math

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
line = int(raw_input())
print fib(line)
