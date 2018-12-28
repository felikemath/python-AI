import time
def regularexpression(string):
    new = ''
    ans = []
    for i in string:
        if i.isalpha():
           new += i
        else:
            new += ' '
    newlist = new.split(' ')
    final = list(filter(None, newlist))
    for item in final:
        loweritem = item.lower()
        if loweritem.startswith('mi') and loweritem.endswith('l'):
            ans.append(item)
    return ans


bob = 'Miijkdjdl I am mil MIll5llll5 mila a5 tal0nted mItL/ play3r, I am Michael'
start = time.time()
for i in range(1):
    print(regularexpression(bob))
end = time.time()
print(end - start)