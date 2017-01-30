"""
Calculating Number of Inversions in a Permutation using Bit Integer Tree
"""
#Dependecies
import numpy as np

#Bit Integer Tree, add and sum functions
class Bit:
    def __init__(self, n):
        sz = 1
        while n > sz:
            sz *= 2
        self.size =sz
        self.data = [0]*sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

#Calculates number of inversions given an array of integers
def count_inversions(A):
    res = 0
    bit = Bit(max(A)+1)
    for i, v in enumerate(A):
        res += i - bit.sum(v)
        bit.add(v, 1)
    return res

#Converts integer into array
def split(num):
    return np.asarray(map(long, str(num)))


#User I/O
user_input = input("Please input an integer." + "\n")

print ("Number of inversions to sequentially sort digits:")
iterable = split(user_input)

print(count_inversions(iterable))

