# Factorial calulation using while loop

num = int(input("Enter a number: "))        #take input from user and store in num named variable

factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i  = i + 1

print("Factorial of", num, "is", factorial)