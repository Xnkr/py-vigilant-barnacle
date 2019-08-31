a = [1,2,3]
b = [2,3,4]
y = 5
x = 1

try:
    a[x] = b[y]
except IndexError:
    try:
        a[x]
        print('b out of index')
    except IndexError:
        print('a out of index')
