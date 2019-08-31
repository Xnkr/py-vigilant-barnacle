N = 10
M = 10
X = [2,7,5,9,6,1,8,10,3,4]

min_n = 1
max_n = N
in_val = []
for i in X:
    if i not in in_val:
        in_val.append(i)
    ranges = []
    for idx, e in enumerate(in_val):
        test_val = in_val[0:idx] + in_val[idx+1:]
        min_v = -1
        max_v = -1

        if len(test_val) == 0:
            min_v = min_n
            max_v = max_n

        if e-1 in test_val:
            min_v = e
        if e+1 in test_val:
            max_v = e
        

        if min_v == -1 or max_v == -1:
            sort_v = sorted(test_val)
            if min_v == -1:
                if sort_v[0] > e:
                    min_v = min_n
                else:
                    for k in sort_v:
                        if k > e - 1:
                            break
                        min_v = k + 1
            if max_v == -1:
                if sort_v[-1] < e:
                    max_v = max_n
                else:
                    for k in sort_v[::-1]:
                        if k < e + 1:
                            break
                        max_v = k - 1

        ranges.append(min_v)
        ranges.append(max_v)
    print(sum(ranges))
    

