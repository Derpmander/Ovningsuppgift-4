import random #importerar random
n=0 
while n!=0 or 10 or -10:#gör så at koden loppar tills en nolla eller 10 eller -10 dycker up
    n=random.randint(-10,10)#skriver ut random tal från -10 till 10
    print(n)#printar talen
    if n==0 or n==10 or n==-10:#avslutar lopen och börjar nästa del om en nlla eller 10 eller -10 skrivs
        a=int(input("Give me the biggest number: "))#Frågar efter den största
        b=int(input("Give me the smallest number: "))#Frågar efter det minsta talet
        if b <=0:
            print("Smallest number", a)#skriver ut det minsta talet
            print("Biggest number", b)#skriver ut det största talet