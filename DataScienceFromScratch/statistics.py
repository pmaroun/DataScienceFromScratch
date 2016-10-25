from collections import Counter
from linear_algebra import sum_of_squares, dot
import math
import matplotlib.pyplot as plt

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

##def make_friend_counts_histogram(plt):
friend_counts = Counter(num_friends)
print(friend_counts)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0,101,0,25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
## plt.show()

num_points = len(num_friends) #204
largest_value = max(num_friends) #100
smallest_value = min(num_friends) #1
sorted_values = sorted(num_friends)
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2] #49

def mean(x):
    return sum(x) / len(x)

print("mean")
print(mean(num_friends))

print("median")
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n //2

    if n % 2 == 1:
        #if odd return middle value
        return sorted_v[midpoint]
    else:
        # if even return the averageof the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print (median([1,2,3,4,5,6]))

print("Quantile")
def quantile(x, p):
    """returns the pth percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print(quantile(num_friends, 0.10)) #1
print(quantile(num_friends, 0.25)) #3
print(quantile(num_friends, 0.50)) #6
print(quantile(num_friends, 0.90))  #13

print ("mode")
## most common values
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.most_common()
            if count==max_count]

print(mode(num_friends))
