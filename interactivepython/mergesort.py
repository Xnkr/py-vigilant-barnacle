def mergesort(alist):
    print alist
    if len(alist) > 1:

        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i+=1 

            else:
                alist[k] = righthalf[j]
                j+=1 

            k+=1

        while i < len(lefthalf):

            alist[k] = lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):

            alist[k] = righthalf[j]
            j+=1
            k+=1

        print alist, lefthalf, righthalf

import numpy as np
alist = [int(i) for i in (np.random.randn(10)*np.random.randint(100)//1).tolist()]
alist = range(5,0,-1)
mergesort(alist)
print(alist)
