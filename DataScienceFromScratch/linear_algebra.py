import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot
from collections import defaultdict, Counter
from functools import partial, reduce

print("linear algebra -- vectors")

height_weight_age = [70,    # inches 
                     170,   # pounds
                     40]    # years

grades = [95,   #exam 1
          80,   #exam 2
          75,   #exam 3
          62]   #exam 4

print("zip")
print("python3 returns an iteration.. python 2 returned a list. .Using the list function to return a list")
print(list(zip([4,5,6], [7,8,9])))
print(list(zip({4,5,6}, {7,8,9}))) ## this doesn't order the second set properly because python doesnt guarantee the order.  keys are hashed

print("python3 zip iteration usage")
zipped_list = zip([4,5,6], [7,8,9])
for pair in zipped_list:
    print(pair)

print("add two vectors")
def vector_add(v, w):
        return [v_i + w_i
                for v_i, w_i in zip(v, w)]

print(vector_add([1,2,3], [4,5,6]))                  
print(vector_add([4,5,6], [7,8,9]))                  

print("subtract two vectors")
def vector_subtract(v, w):
        return [v_i - w_i
                for v_i, w_i in zip(v, w)]
print(vector_subtract([1,2,3], [4,5,6]))                  

print("sum x vectors")
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:  # loop over the others
        result = vector_add(result, vector)
    return result
print(vector_sum([[1,2,3], [4,5,6], [7,8,9]]))                  

print("sum x vectors using reduce")
def vector_sum_2(vectors):
    return reduce(vector_add, vectors);
print(vector_sum_2([[1,2,3], [4,5,6], [7,8,9]]))                  

print("scalar multiply")
## c * [a1, a2, an]
def scalar_multiply(c,v):
    return [c * v_i for v_i in v]
print(scalar_multiply(2, [1,2,3]))

print("vector mean")
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
print (vector_mean([[1,2,3], [4,5,6], [7,8,9]]))

print("dot product")
### signify dot product by v.w
### v1*w1 + v2*w2 + vn*wn
### [2,7].[7,1]
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i 
               for v_i, w_i in zip(v, w))
print(dot([1,2], [1,4]))

print("magnitude or length")
###  ||v|| = sqrt of ( v1(squared) + v2(squared) + v3(squared) )
### or
###  ||v|| = sqrt of ( v.v )
### or
###  ||v||(squared) = v.v
def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))
print(magnitude([2,5])) ## sq root of 29

print("distance between two vectors")
### euclidean distance
### d(v, w) = sqrt ( ((v1 - w1)squared) + (v2 - w2)squared) + (vn - wn)squared)

def squared_distance(v,w):
    """(v_1 - w_1) ** 2 + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v,w))
def distance(v, w):
    ## return math.sqrt(squared_distance(v, w)) or
    return magnitude(vector_subtract(v, w))

print(distance([1,2], [3,4]))

print("linear algebra -- matrices")

print("get matrix shape")
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols
print(shape([[1,2,3], [4,5,6]]))

print("get matrix vector")
def get_row(A, i):
    return A[i]

def get_col(A, j):
    return [A_i[j] 
        for A_i in A]

print (get_row([[1,2,3], [4,5,6]], 1))
print (get_col([[1,2,3], [4,5,6]], 1))

print("make matrix")
def make_matrix(num_rows, num_cols, entry_fn):
    """returns an num_rows, num_cols matrix"""
    """whos (r,c) entries are entry_fn(r,c)"""
    return [[entry_fn(r, c)
            for r in range(num_rows)]
            for c in range(num_cols)]
            
def is_diagonal(r, c):
    """1's on the diagonal 0's everywhere else"""
    return 1 if r==c else 0

print (make_matrix(5, 5, is_diagonal))





