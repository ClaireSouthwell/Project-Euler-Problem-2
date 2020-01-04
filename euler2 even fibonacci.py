# Project Euler problem 2: Even Fibonacci Numbers
# By considering the terms in the Fibonacci sequence that do not
# exceed the nth term, find the sum of the even-valued terms
# The function should always return an even value 

def fiboEvenSum(number):
    # Given the first 2 numbers of the sequence as 1 and 2
    fibs = [1, 2]
    
    #Get the fibs up to the given number
    while len(fibs) < number: 
        fibs.append(fibs[-1] + fibs[-2])
    
    #Loop through the list adding only the even fibs to the total
    total = 0
    for item in fibs:
        if item % 2 == 0:
            total += item
    
    return total        
            
# TESTS        

print('fiboEvenSum(10) should return 44:')
print(fiboEvenSum(10))

print('fiboEvenSum(18) should return 3382:')
print(fiboEvenSum(18))

print('fiboEvenSum(23) should return 60696:')
print(fiboEvenSum(23))

print('fiboEvenSum(43) should return 350704366:')
print(fiboEvenSum(43))
