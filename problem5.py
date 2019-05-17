# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#n= 9*8*7*6*5*4*3*2
# n =24


# print (n)
# fct=[]
# for i in range(2, 10):
#     while n%i==0:
#         n=n/i
#         fct.append(i)
#         print(n, fct)
cnt=0
list = list(range(2,11))
for i in range(2, 11):
    for idx, e in enumerate(list):
        while idx < 8 and cnt!=1:
            if e%i==0:
                if e//i==1:
                    cnt==1
                cnt==0
                break

                print (idx, i, e)
            
