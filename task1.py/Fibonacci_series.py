# print fibonacci series 

n = int(input("Enter the number of terms :"))       #taking input from user
a = 0
b = 1

if n < 0:
    print("Fibonacci series :")
    print("Enter a positive number !")

elif n == 1:
    print("Fibonacci Series :")
    print(a)

else :
    print("Fibonacci Series :")
    print(a, end= " ")
    print(b, end= " ")

    for i in range (2, n):
        c = a + b
        print(c, end= " ")
        a = b
        b = c