def factorial(n):
  if n == 1:
    return n
  else:
    return n*factorial(n-1)

#taking input from the user
num = int(input("enter any number:"))

# if the user inputs a negative integer
if num < 0:
   print("factorial does not exist for negative numbers")
#if the user inputs 0
elif num == 0:
   print("the factorial of 0 is 1")
else:
   print("the factorial of",num,"is",factorial(num))
                       