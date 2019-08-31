t = [1,'','',2,'','','',3,'']

new_list = []

keep = False
for idx, element in enumerate(t):
    if element is not '':
        keep = True
        new_list.append(element)
        continue
    
    if keep:
        new_list.append(element)
    keep = not keep

print(new_list)

from itertools import groupby

l = [1,'','',2,'','','',3,'']

new_list = []
for v, g in groupby(l):
    new_list += list(g) if v != '' else list(g)[:-1]

print(new_list)