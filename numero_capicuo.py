



#input
n=int(input("digite un numero: "))

#procesing
if n<100000 and n>9999:
    m=n%100
    c=n//1000
    r=c%10
    d=c//10
    b=m%10
    x=m//10



    if x==r and b==d:
        print("es un numero oblicuo")
    else: 
        print("no es un numero oblicuo")
else:
    print("no es un numero de 5 digitos")

