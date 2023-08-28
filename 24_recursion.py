# Recursion means function call written in same function 
# factorial 7 = 7*6*5*4*3*2*1
# factorial 6 = 6*5*4*3*2*1
# factorial n = n * factorial(n-1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(3)) 
# print(factorial(4)) 
# print(factorial(5))

# Fibonacci number

def fibonacci(a):
    if a<=1:
      return a
    else:
       return (fibonacci(a-1) + fibonacci(a-2))


for i in range(7):
   print(fibonacci(i))
