lst = [23,52,44,32,78]

lsts = {frozenset(str(x)):x for x in lst}
no_shared_digits = [l for l in lsts if all(x.isdisjoint(l) for x in lsts if x != l)]

result = [lsts[x] for x in no_shared_digits]