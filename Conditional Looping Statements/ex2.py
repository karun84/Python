age=int(input("Enter your age: "))
full_price=6
if age<16:
    price=full_price/2
    print(f"Your ticket costs £{price}")
elif age>=60:
    price=full_price/3
    print(f"Your ticket costs £{price}")        
else:
    print(f"Your ticket costs £{full_price}")    