import math
import random
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
    return prob.inverse_normal_cdf(1 - probability, mu, sigma)

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

print("flipping an even coin hypothesis")
# null hypothesis is that coin is fair (p = 0.5)
# test this against p != 5

print("Using a fair coin")
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print(mu_0, sigma_0)
lo, hi = normal_two_sided_bounds(.95, mu_0, sigma_0)
print(lo, hi) #(469, 531)

print("Using an unfair coin")
# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

#actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
print(mu_1, sigma_1)
# a type 2 error means we fail to reject the null hypothesis
# which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)

## power of a test is the probability of not making a type 2
power = 1 - type_2_probability #0.887
print(power)

# null hypothesis is that the coin is not biased towards heads or that p<=0.5
# we want a one-sided test that rejects the null hypothesis when 
# X is much larger than 50 but not when X is smaller than 50
hi = normal_upper_bound(0.95, mu_0, sigma_0)
# is 526 ( <531 since we need more probability in the upper tail)
print (hi)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability #.936
print (power)

def two_sided_p_value(x, mu=0, sigma=1):
    if x>=mu:
        #if x is greater than the man, the tail is whats greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)

print("two-sided p-value")
# if we were to see 530 heads we would compute..    
#mu_0=500 sigma_0= 15.73
print(two_sided_p_value(529.5, mu_0, sigma_0)) #0.062
##note that 529.5 is a continuity correction.  

print("example to prove the above .062")
#extreme_value_count = 0
#for __ in range(10000):
#    num_heads = sum(1 if random.random() < 0.5 else 0 ##count # of heads
#                    for __ in range(1000)) ## in 1000 flips
#    if num_heads >= 530 or num_heads <= 470: 
#        extreme_value_count +=1
#print (extreme_value_count / 10000) #0.062

print ("p hacking")
def run_experiment():
    """flip a fair coin 1000 times"""
    return [random.random() < 0.5 for __ in range(1000)]

def reject_fairness(experiment):
    """using 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads <469 or num_heads>531

random.seed(0)
expiriments = [run_experiment() for __ in range(1000)]
num_rejections = len([experiment 
                      for experiment in expiriments
                      if reject_fairness(experiment)])

print(num_rejections) ##46

print ("A/B test for ad clicks")
## null hypotheses each add will get equal clicks
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 -p) / N)
    return p, sigma
def a_b_test_statistics(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A **2 + sigma_B ** 2)

z = a_b_test_statistics(1000, 200, 1000, 180) #-1.14
print(two_sided_p_value(z))  #.254

z = a_b_test_statistics(1000, 200, 1000, 160) #-2.94
print(two_sided_p_value(z))  #.003

print ("bayesian inference")

