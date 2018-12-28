def print_cool():
    print('I am the coolest person in the world')

def weird_func():
    print('my python function')


def addfunction(a, b):
    return a + b

def printstring(string='Nothing'):
    print('This function prints the string that was inputted: %s' % string)

while True:
    answer = input('I am an echo machine, I am glad to meet you. If you want to exit this conversation, type bye: ')
    if answer == 'bye':
        print('It was nice talking to you :(')
        break
    print("You just said, '%s'" % answer)



print_cool()
weird_func()
x = 1
y = 2
print('the sum of %d and %d is %d' %(x, y, addfunction(x, y)))
printstring()
