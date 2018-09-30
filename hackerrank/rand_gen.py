import random as rd

base = list(map(chr,range(97,123))) + [str(x) for x in range(0,10)] + list(map(chr,range(65,91)))
base = "".join(base)

res = ""
while len(res)<51:
 res += base[rd.randrange(len(base))]
print res
