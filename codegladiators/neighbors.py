import heapq


def heapSum():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tickets = list(map(int, input().split()))
        inv_tickets = [-1*i for i in tickets][::-1]
        res = [0] * len(tickets)
        heapq.heapify(inv_tickets)
        if _ == 3:
            print(inv_tickets)
        l_idx = c_idx = -1
        l_pop = c_pop = -1
        while len(inv_tickets) > 0:
            c_pop = -1 * heapq.heappop(inv_tickets)
            if c_pop <= 0:
                break
            c_idx = tickets.index(c_pop)
            if l_idx == -1:
                l_idx = c_idx
                l_pop = c_pop
                res[l_idx] = l_pop
            else:
                srch_idx = (l_idx-1, l_idx+1)
                if c_idx in srch_idx:
                    continue
                l_idx = c_idx
                l_pop = c_pop
                res[l_idx] = l_pop

        r = [str(x) for x in res if x > 0][::-1]
        print(''.join(r))


mem = {}
def findSum(a, idx):

    if idx >= len(a):
        return (0,[])

    if idx in mem:
        return mem[idx]
    
    sum_after_take, take_items = findSum(a, idx+2) 
    take = a[idx] + sum_after_take
    sum_after_skip, skip_items = findSum(a,idx+1)
    skip = sum_after_skip
    if take > skip:  
        take_items.append(a[idx])
        mem[idx] = (take,take_items)
        return (take,take_items)
    elif take == skip:
        take_items.append(a[idx])
        if len(take_items) > 1 and len(skip_items) > 1:
            if take_items[0] > skip_items[0]:
                mem[idx] = (take,take_items)
                return (take,take_items)
            else:
                mem[idx] = (skip,skip_items)
                return (skip,skip_items)    
        else:
            mem[idx] = (take,take_items)
            return (take,take_items)
    else:
        mem[idx] = (skip,skip_items)
        return (skip,skip_items)

def main():

    t = int(input())
    for _ in range(t):
        input()
        a = list(map(int,input().split()))
        h = list(map(str,findSum(a,0)[1]))
        print(''.join(h))



#main()



print(findSum([-1,7,8,-5,4,6,10],0))
mem = {}
print(findSum([4,5,4,3],0))
mem = {}
print(findSum([4,4,4,50,4,4,4,50,50],0))