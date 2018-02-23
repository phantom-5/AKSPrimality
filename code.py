import math


print("Implements AKS Primality Test")


print("Enter lower bound(Inclusive): ")
global l
l=int(input())
print("Enter upper bound(Exclusive): ")
global u
u=int(input())




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
        if aks(l) is True and l!=1:
            print(l)
    l=l+1

