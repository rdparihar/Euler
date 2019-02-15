#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


a=1
b=2

sm=0



while b < 4000000:
    c = a+b
    a = b
    b = c
   # print (a, "-----",b)
    if a%2==0:
        print (a)
        sm=sm+a
print ("sum", sm)
