sizeOfSet=int(input("Please enter the size of the set:"))
i=0

sampleList = [] # Create a list
while i < sizeOfSet:
    element=input("Enter the element of the set:")
    sampleList.append(element)
    print(sampleList)
    i += 1

# The maximum number of subset is 2^n, where n is the size of the set
numberOfSubset = pow(2,sizeOfSet)

# count is the number that we want to reach
for count in range(0, numberOfSubset):
    for n in range(0,sizeOfSet):
        # IF statement is used to
        # check if nth bit in the
        # count have to be set or not. ( Think in binary representation)
        # If the nth bit have to be set,
        # then print the nth element from set
        # 1 << n is 2^n, when n=0, 1->2, 2->4
        # & is bitwise and, for example 6 is 110
        # when compare 110 & 001, false, don't print
        # 110 & 010, true, print
        # 110 & 100, true, print
        if (count & (1 << n)) > 0:
            print(sampleList[n],end="")
    print("")
