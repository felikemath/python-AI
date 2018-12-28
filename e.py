# There is a bank, giving you a APR 6% for your saving account. If you have $1 at the beginning. Please use python to calculate how much you will have after 10 years
import math
start = 1
percent = 6 #%
years = 12
def apr(init, percent, years):
    total = init * math.pow(1+percent/100, years)
    return total

print(apr(start, percent, years))
N = 10000000
print((1 + 1/N)**N)
n = 0.0000001
print((1+n)**(1/n))
total = 1
n = 100
for i in range(n):
    total *= (1+(1/n))
    print(math.e - total)

print(total)
print(math.e)