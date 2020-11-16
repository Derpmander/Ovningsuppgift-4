import random
n=0
while n!=1:
    n=random.randint(1,10)
    print(n)
    if n==1:
        a=int(input("Give me the smallest number: "))
        b=int(input("Give me the biggest number: "))
        c=int(input("Negative number now: "))
        if c <=0:
            print("Smallest number", a)
            print("Biggest number", b)