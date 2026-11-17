from scipy.stats import binom
 
n, p = 10, 0.5

exact = binom.pmf(6, n, p)

cumulative = binom.cdf(6, n, p)

samples = binom.rvs(n, p, size=5)

print("Exact:", exact)
print("Cumulative:", cumulative)
print("Random samples:", samples)

