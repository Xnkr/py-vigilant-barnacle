from __future__ import division
import math

def moving_shift(s, shift):
    cipher = []
    for c in s:
        if c.isalpha():
            if c.isupper():
                z = 'Z'
                a = 'A'
            else:
                z = 'z'
                a = 'a'
            if ord(c) + shift > ord(z):
                to_shift = (shift - (ord(z) - ord(c)))%26
                if to_shift == 0:
                    to_shift = 26

                cipher.append(chr(ord(a)+to_shift - 1))
            else:
                cipher.append(chr(ord(c)+shift))
        else:
            cipher.append(c)
        shift += 1
    cipher_str = ''.join(cipher)
    l = len(cipher)
    split_len = int(math.ceil(l/5))
    result = [cipher_str[i:i+split_len] for i in range(0, l, split_len) ]
    if len(result) < 5:
        result += [''] * (5-len(result))
    return result


def demoving_shift(s, shift):
    s = ''.join(s)
    cipher = []
    for c in s:
        if c.isalpha():
            if c.isupper():
                z = 'Z'
                a = 'A'
            else:
                z = 'z'
                a = 'a'
            if ord(c) - shift < ord(a):
                to_shift = (shift-(ord(c) - ord(a)))%26
                if to_shift == 0:
                    to_shift = 26

                cipher.append(chr(ord(z)-to_shift + 1))
            else:
                cipher.append(chr(ord(c)-shift))
        else:
            cipher.append(c)
        shift += 1
    return ''.join(cipher)

print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1) == ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"])
print(demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"], 1) == "I should have known that you would have a perfect answer for me!!!")