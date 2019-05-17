
def is_prime(n):
    count= 0
    for i in range (2, n+1):
        count= count+1
        print(count)  
        if n%i==0:
            while n%i==0 and n//i!=1:
                n=n//i              
            if n==i:
                return (i)
           
#n=600851475143
#is_prime(n)               
print("Largest:", is_prime(int(input("Enter the number-"))))


# import unittest 
  
# class SimpleTest(unittest.TestCase): 
  
#     # Returns True or False.  
#     def test(self):         
#         self.assertTrue(6857==is_prime(n) ) 
  
# if __name__ == '__main__': 
#     unittest.main() 
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