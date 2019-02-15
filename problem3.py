
def is_prime(n):
    for i in range (2, n+1):
        if n%i==0:
            while n%i==0 and n//i!=1:
                n=n//i              
            if n==i:
                return (i)
print("Largest:", is_prime(int(input("Enter the number-"))))

# if n %2!=0:
#     print (is_prime(n))
# elif n==2:
#     print (n)
# else:
#     while n%2==0 and n//2!=1:
#         n=n//2
#         if n==2:
#             print (n)
#         if n %2!=0:
#             print (is_prime(n))
# n= 6008514751432