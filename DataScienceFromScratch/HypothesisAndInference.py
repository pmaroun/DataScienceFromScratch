import math

import sys
sys.path.append("data-science-from-scratch-master\code_python3")

import probability as prob

print ("hypothesis and inference")

def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a binomial (n,p)"""
    mu = p * n
    sigma = math.sqrt(p * (1-p) * n)
    return mu, sigma

# the normal cdf is the probability the variable is below a threshold
normal_probability_below = prob.normal_cdf

# it's above the threshold if its not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - prob.normal_cdf(lo, mu, sigma)

#it's between if it's less tha nhi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return prob.normal_cdf(hi, mu, sigma) - prob.normal_cdf(lo, mu, sigma)

#its outside if its not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1-normal_probability_between(lo, hi, mu, sigma)

print ("normal probability")
below = normal_probability_below(.5, 0, 1)
print(normal_probability_below(.5, 0, 1)) # .69
print(normal_probability_above(.5, 0, 1)) #.31
print(normal_probability_between(.3, .7, 0, 1)) #.14
print(normal_probability_outside(.3, .7, 0, 1)) #.86

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns z for which P(Z <= z) = probability"""
    return prob.inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns z for which P(Z >= z) = probability"""
    return prob.inverse_normal_cdf(probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the means) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    #upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    #lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

print(normal_lower_bound(below, 0, 1))


