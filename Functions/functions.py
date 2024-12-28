#1st question
#len() function return the length of an object.
example=[2,3,4,5,6,7,8]

length=len(example)
print("Length of the list is:",length)

#2nd question
def greet(name):
    print("Hello, " + name)

greet("karun")   


#3rd question

example=[2,3,4,5,6,77]
def find_maximum(numbers):
    largest=example[0]
    for num in example:
        if num>largest:
            largest=num
    print(largest)        


print(find_maximum(example))

#4th question
"""local variables are declared inside functions whereas global variables are declared outside functions."""

a=20

def exmp():
    a=40
    print("Local variable a:",a)

exmp()
print("Global variable a:",a)

#5th question

def calculate_area(length, width=5):
    return length * width


print("with width 6: ",calculate_area(10,6))    

print("without width: ",calculate_area(10))