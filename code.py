import math


print("Implements AKS Primality Test with memoization using dictionary")


print("Enter lower bound(Inclusive): ")
global l
l=int(input())
print("Enter upper bound(Exclusive): ")
global u
u=int(input())


dict={0:False}


def ncr(n,r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))


def aks(a):
    for i in range(1,a+1):
        if i!=a:
            if ncr(a,i)%a!=0:
                return False

    return True

print("The primes are: ")
while(l<u):
    if l%2!=0:
        k=dict.get(l,0)
        if dict[k] is True:
            print(l)
        elif aks(l) is True and l!=1:
            print(l)
            dict[l]=True

    l=l+1

