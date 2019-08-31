def is_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

# Complete the almostSorted function below.
def almostSorted(arr):
    left_unsorted = -1

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            left_unsorted = i
            break
    
    if left_unsorted == -1:
        print("yes")
        return

    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            # Try with swapping
            new_arr = arr[:]
            new_arr[left_unsorted], new_arr[i] = new_arr[i], new_arr[left_unsorted]
            if is_sorted(new_arr):
                print("yes")
                print("swap",left_unsorted + 1,i+1)
                return
            
            new_arr = arr[:]
            new_arr[left_unsorted:i+1] = new_arr[left_unsorted:i+1][::-1]
            if is_sorted(new_arr):
                print("yes")
                print("reverse", left_unsorted + 1,i + 1)
                return

            print("no")


arr = lambda t: list(map(int, t.split()))
almostSorted(arr('3 1 2'))
almostSorted(arr('4 2'))
almostSorted(arr('1 5 4 3 2 6'))
