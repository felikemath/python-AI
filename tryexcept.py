def compare_ints(t):
    """t is tuple"""
    #clean up tuple\
    new_t = tuple()
    num_args = 0
    for i in t:
        if i.isdigit():
            new_t += (i,)
            num_args += 1
    if num_args != 2:
        raise IncorrectAmountofNumbers
    x, y = int(new_t[0]), int(new_t[1])
    if x > y:
        print('%d is greater than %d' % (x, y))
    elif x == y:
        print('They are the same value')
    elif y > x:
        print('%d is greater than %d' % (y, x))

class IncorrectAmountofNumbers(Exception):
    pass

while True:
    try:
        t = tuple(input('Hello! I am KINGEDWARDBOT and I like to compare values. Type bye if you want to leave. Please input two values to be compared:\n '))
        if t == tuple('bye'):
            print('Nice talking to you, KINGEDWARDBOT OUT!!')
            break
        compare_ints(t)
    except IncorrectAmountofNumbers:
        print('You have inputted an incorrect number of numbers')
    except:
        print('please input a valid tuple of integers')


