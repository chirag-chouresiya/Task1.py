str = input("Enter a string : ")
reverse = str[::-1]
print("Reversed string is:", reverse)

if str == reverse:
    print("This string is palindrome :")

elif str != reverse:
    print("This string is not a palindrome")