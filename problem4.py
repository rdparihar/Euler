# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# result 906609

def reverse(n):
    rev = 0 
    while(n > 0):    
        rem = n %10    
        rev = (rev *10) + rem    
        n = n //10    
    return (rev)     

def is_palindrome():
    y=900000
    for i in range(999, 900, -1):
        for j in range (999, 900, -1):
            x=str(i*j)
            if i*j == reverse(i*j):
                print ("gehjhj", i*j)
            if x[:1]==x[-1:] and x[1:2]==x[-2:-1] and int(x[:1]) > 7:
               
                if x[2:3]==x[-3:-2] and len(x)>= 6:
                    print (x, i, j)
                    if int(x) > y:
                        print (x)
                        x=y
                    
                    
                else:
                    break

                #return (x, i, j)  
                #   

 


print ("Largest factor is :",is_palindrome())




















# Python code to demonstrate working of unittest 
# import unittest 
  
# class TestStringMethods(unittest.TestCase): 
      
#     def setUp(self): 
#         pass
  
#     # Returns True if the string contains 4 a. 
#     def test_strings_a(self): 
#         self.assertEqual( 'a'*4, 'aaaa') 
  
#     # Returns True if the string is in upper case. 
#     def test_upper(self):         
#         self.assertEqual('foo'.upper(), 'FOO') 
  
#     # Returns TRUE if the string is in uppercase 
#     # else returns False. 
#     def test_isupper(self):         
#         self.assertTrue('FOO'.isupper()) 
#         self.assertFalse('Foo'.isupper()) 
  
#     # Returns true if the string is stripped and  
#     # matches the given output. 
#     def test_strip(self):         
#         s = 'geeksforgeeks'
#         self.assertEqual(s.strip('geek'), 'sforgeeks') 
  
#     # Returns true if the string splits and matches 
#     # the given output. 
#     def test_split(self):         
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world']) 
#         with self.assertRaises(TypeError): 
#             s.split(2) 
  
# if __name__ == '__main__': 
#     unittest.main()