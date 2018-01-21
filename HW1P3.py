#Problem 3: Iterative and Recursive Operations. Write an iterative function and a recursive function that computes the sum of all numbers from 1 to n, where n is given as parameter. Test both functions for n = 100.
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
