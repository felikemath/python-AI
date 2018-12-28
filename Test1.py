class A(object):
    count = 0
    def __init__(self, a=[]):
        self._a = a
        print('._a id: ', id(self._a))
        print('a.count: ', id(A.count))
        # A.count += 1
    def __setattr__(self, key, value):
        self.__dict__[key] = value

y = A(['apple'])

x = y
print(id(x))
print(id(y))



