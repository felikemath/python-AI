def testarguments(a):
    print('before increment id(a) = %d' % id(a))
    a += 1
    print('after increment id(a) = %d' % id(a))

num = 9

print('id(num) = %d' % id(num))
print('before call function, num= %d' % num)
testarguments(num)
print('id(num)= %d' % id(num))
print('after call function, num= %d' % num)
