#Problem 3: Iterative and Recursive Operations
#iterative operation
def iterative(n):
    mysum = 0
    for i in range(1,n+1):
        mysum += i
    return(mysum)

print(iterative(100))


# recursive operation
def fact(n):
    if n == 1:
        return 1
    else:
        return n + fact(n - 1)


print(fact(100))
