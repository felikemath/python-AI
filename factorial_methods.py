#for loop for factorial
product = 1
num = 7
for x in range(1, num + 1):
    product *= x


print(product)

#while loop factorial
init_i = 10
i = 10
product = 1
while i > 0:
    product *= i
    i -= 1


print('The factorial of %d is %d' % (init_i, product))

#factorial function with recursion

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print('The factorial of %d is %d' % (10, factorial(10)))