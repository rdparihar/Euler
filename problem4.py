# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# result 906609

def is_palindrome():
    pd=[]
    for i in range(999, 900, -1):
        for j in range (999, 900, -1):
            x=str(i*j)
            if x[:1]==x[-1:] and x[1:2]==x[-2:-1] :
                if x[2:3]==x[-3:-2]:# and len(x)>= 6:
                    pd.append(x)
                else:
                    break
       # print (pd)
    pd.sort(reverse=True)
    #print (pd)
    return (pd[0])

print ("Ans- '", is_palindrome(),"'is largest palindrome made from the product of two 3-digit numbers")




# def reverse(n):
# #     rev = 0 
# #     while(n > 0):    
# #         rem = n %10    
# #         rev = (rev *10) + rem    
# #         n = n //10    
# #     return (rev)     
# # if i*j == reverse(i*j):
# #                 #print ( i*j)
# #                 pass

