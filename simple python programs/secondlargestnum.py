num1 = int(input("Enter a number:"));
num2 = int(input("Enter another number:"));
num3 = int(input("Enter a number:"));
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        secondlargest = num2
    else:
        secondlargest = num3
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        secondlargest = num1
    else:
        secondlargest = num3
else:

    if num1 >= num2:
        secondlargest = num1
    else:
        secondlargest = num2
print("The second largest number is:", secondlargest)
