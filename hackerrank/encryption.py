import math

def encryption(s):
    res = ''
    c = math.ceil(math.sqrt(len(s)))
    return ' '.join([s[i::c] for i in range(c)])

print(encryption('haveaniceday'))