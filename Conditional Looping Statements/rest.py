num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")


number=int(input("Enter a number: "))
factorial=1
for i in range(1, number+1):
    factorial *=i
print(f"Factorial of {number} is {factorial}")

number=int(input("Enter a number: "))
reversed=0
while number!=0:
    remainder=number%10
    reversed=reversed*10+remainder
    number=number//10

print(f"The reverse of {number} is {reversed}")   



while True:
    word=input("Enter a word: ")
    if word=='done':
        print("Done")
        break
    print(word)
