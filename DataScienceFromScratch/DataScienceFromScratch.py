from __future__ import division
import re
from collections import defaultdict
from collections import Counter

import random

from functools import partial


#for i in [1, 2, 4, 5]:
#    print i
#    for j in [9, 8, 7, 6]:
#        print j
#        print i + j
#    print "end i"

def double (x):
    return x * 2

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)

print x

y = apply_to_one(lambda x: x + 4)
print y

int_list = [1,2,3]
het_list = ["string", .1, True]
list_of_lists = [ int_list, het_list, [] ]
print list_of_lists
print list_of_lists.append([ 4, 5, 6]) ## none 
print list_of_lists
print len(list_of_lists)
## print sum(list_of_lists)
ext = [1,2,3]
print ext
print ext.extend([4,5,6])  # none
print ext

my_list = [1,2]
my_tuple = (1, 2)

x, y = my_list
print x,y
y, x = x,y
print x,y

empty_dict = {}

grades = { "Jim": 4.0, "Pete": 3.0 }

petes_grades = "Pete" in grades

print petes_grades
print grades["Pete"]
print grades.get("Pete", 0)

int_dd_list = defaultdict(int)
print int_dd_list
int_dd_list["pete"] = { "name": "Pete", "phone": "3091111111", "age": 26 }
print int_dd_list

print int_dd_list["pete"]

c = Counter([0,1,2,3,2])
print c

c2 = Counter("hello world hello");
print c2

set = set(c2)
print set

s = "Sting"
print 1 and s[1] ## and returns second value when the 1st is truthy

x=None
safe_x = x or 0
print safe_x

even_numbers = [x for x in range(5) if x % 2 ==0]
print even_numbers

squares = [x * x for x in range(5)]
print squares

square_dict = { x : x * x for x in range(5) }
print square_dict

square_set = { x * x for x in [1, -2, 2, 1] } ## ???
print square_set


four_uniform_randoms = [random.random() for __ in range(4) ]
print four_uniform_randoms

r = random.randrange(1000)
print r

class MySet:
    def __init__(self, values = None):
        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)
            
    def __repr__(self):
        return "MySet: " + str(self.dict.keys())

    def add (self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

set1 = MySet([1, 2, 3, 2])

print set1    

def double (x):
    return x * 2

def exp(base, power):
    return base ** power

xs = [1, 2, 3, 4]

twice_xs = [double(x) for x in xs]
print twice_xs

twice_xs = map (double, xs)
print twice_xs

two_to_the = partial(exp, 2)
print two_to_the(4)

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
plt.plot(years,  gdp, color='green', marker='o', linestyle='solid')
plt.title ("Nominal GDP")
plt.ylabel ("Billion of $$")
## plt.show() ##

gpa1 = [3.2, 3.3, 1.9, 2.5, 2.6, 2.7, 2.3]
gpa2 = [3.2, 3.8, 1.7, 2.8, 2.6, 1.7, 1.3]
gpa3 = [2.2, 2.8, 2.7, 2.8, 2.6, 2.7, 2.3]

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
        for v_i, w_i in zip(v,w)]

print "add vectors"
print vector_add(gpa1, gpa2)
    
def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

vectors = [gpa1, gpa2, gpa3]

print "sum vectors"
print vector_sum(vectors)

print "reduce vectors (add)"
print reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number v is the vector"""
    return [c *v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

print "vector mean"
print vector_mean(vectors)

def dot(v, w):
    """ v_1 + w_1 + ... + v_n + w_n *w_n """
    return sum(v_i * w_i for v_i, w_i in zip(v,w)) 

print "dot"
print dot(gpa1, gpa2)

def make_matrix(num_rows, num_cols, entry_fn):
    """ returns a num_rows x num_cols matrix """
    """ whos (i,j) entry is entry_fn(i,j) """
    return [[entry_fn(i,j)
        for j in range (num_cols)]
        for i in range (num_rows)]

print make_matrix(2, 2, sum)

    

        
