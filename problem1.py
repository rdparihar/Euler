# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# method1
import datetime

start=datetime.datetime.now()

range_list = list(range (100000))
#print (range_list)
s=0
for number in range_list:
    if number%3==0 or number%5==0:
        s = s+number
print (s)
end=datetime.datetime.now()

print (end-start)
# 3*int(999/3)*(1+int(999/3))/2 + 5*int(999/5)*(1+int(999/5))/2 - 15*int(999/15)*(1+int(999/15))/2
start1=datetime.datetime.now()
t = 3*(99999//3)*(1+(99999//3))//2 + 5*(99999//5)*(1+(99999//5))//2 - 15*(99999//15)*(1+(99999//15))//2

print(t)
end1=datetime.datetime.now()
print (end1-start1)