data = [[1539841080000,None],[1539841140000,None],[1539841200000,1.07609359e+08],[1539841260000,None],[1539841320000,None],[1539841380000,None],[1539841440000,None],[1539841500000,None],[1539841560000,1.07613162e+08],[1539841620000,None],[1539841680000,1.07613162e+08],[1539841740000,None],[1539841800000,None]]

prev_val = None
new_data = []

for item in data:
    t, d = item
    if d is None and prev_val is not None:
        new_data.append([t,prev_val])
    elif d is not None:
        prev_val = d
        new_data.append(item)

print(new_data)