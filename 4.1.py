import random #importerar random
n=0 
while n!=1:#gör så at koden loppar tills 1 dycker up
    n=random.randint(-10,10)#skriver ut random tal från -10 till 10
    print(n)#printar talen
    if n==1 or n==10 or n==-10:#avslutar lopen och börjar nästa del om en etta skrivs
        a=int(input("Give me the biggest number: "))#Frågar efter den största
        b=int(input("Give me the smallest number: "))#Frågar efter det minsta talet
        if b <=0:
            print("Smallest number", a)#skriver ut det minsta talet
            print("Biggest number", b)#skriver ut det största talet