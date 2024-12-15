
for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  
    elif i % 3 == 0:
        print("Fizz")  
    elif i % 5 == 0:
        print("Buzz")  
    else:
        print(i) 

num=int(input("Enter a number: "))
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()    