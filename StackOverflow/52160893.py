start_inner = 1
end_inner = 4
start_outer = 1
end_outer = 3

for i in range(start_outer,end_outer+1):
    for j in range(start_inner,end_inner+1):
            print("{:>1} {:>1}".format(i,j))
print("After the loop")