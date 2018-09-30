import sys


n,k = [int(x) for x in "6 4".strip().split(' ')]
a = [int(a_temp) for a_temp in "1 3 2 6 1 2".strip().split(' ')]

mods = [0] * k
for i in range(n):
    mods[a[i] % k] += 1 
print mods
count = 0
for i in range(int(k/2) + 1):
    if i == 0:
        count += int(mods[0] * (mods[0] - 1) / 2)
        print int(mods[0] * (mods[0] - 1) / 2)
    elif float(i) == (k/2.0):
        count += int(mods[int(k/2.0)] * (mods[int(k/2.0)] - 1) / 2)
        print int(mods[int(k/2.0)] * (mods[int(k/2.0)] - 1) / 2)

    else:
        count += int(mods[i] * mods[k-i])
        print int(mods[i]), (mods[k-i])
    print "" ,i
print (count)