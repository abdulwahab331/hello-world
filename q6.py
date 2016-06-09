def print_histogram(l):
    for i in range(0,len(l)):
        for j in range(0,l[i]):
            print("*",end='')
        print("\n")
print("Enter the list of integers: ",end='')
l1=[int(i) for i in input()]
print_histogram(l1)

