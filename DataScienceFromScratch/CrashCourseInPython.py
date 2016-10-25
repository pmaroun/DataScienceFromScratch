## Intro Learning Python for Data Science ##

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

print(x)

y = apply_to_one(lambda x: x + 4)
print(y)

int_list = [1,2,3]
het_list = ["string", .1, True]
list_of_lists = [ int_list, het_list, [] ]
print(list_of_lists)
print(list_of_lists.append([ 4, 5, 6])) ## none 
print (list_of_lists)
print (len(list_of_lists))
## print (sum(list_of_lists))
ext = [1,2,3]
print (ext)
print (ext.extend([4,5,6]))  # none
print (ext)

my_list = [1,2]
my_tuple = (1, 2)

x, y = my_list
print (x,y)
y, x = x,y
print (x,y)

empty_dict = {}

grades = { "Jim": 4.0, "Pete": 3.0 }

petes_grades = "Pete" in grades

print (petes_grades)
print (grades["Pete"])
print (grades.get("Pete", 0))

int_dd_list = defaultdict(int)
print (int_dd_list)
int_dd_list["pete"] = { "name": "Pete", "phone": "3091111111", "age": 26 }
print (int_dd_list)

print (int_dd_list["pete"])

c = Counter([0,1,2,3,2])
print (c)

c2 = Counter("hello world hello");
print (c2)

set = set(c2)
print (set)

s = "Sting"
print (1 and s[1]) ## and returns second value when the 1st is truthy

x=None
safe_x = x or 0
print (safe_x)

even_numbers = [x for x in range(5) if x % 2 ==0]
print (even_numbers)

squares = [x * x for x in range(5)]
print (squares)

square_dict = { x : x * x for x in range(5) }
print (square_dict)

square_set = { x * x for x in [1, -2, 2, 1] } ## ???
print (square_set)


four_uniform_randoms = [random.random() for __ in range(4) ]
print (four_uniform_randoms)

r = random.randrange(1000)
print (r)

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

print (set1)

def double (x):
    return x * 2

def exp(base, power):
    return base ** power

xs = [1, 2, 3, 4]

twice_xs = [double(x) for x in xs]
print (twice_xs)

twice_xs = map (double, xs)
print (twice_xs)

two_to_the = partial(exp, 2)
print (two_to_the(4))

