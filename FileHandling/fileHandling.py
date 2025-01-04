#1st question
with open("test.txt","r") as file1:
    content=file1.read()
    print(content)


#2nd question    
starting=input("Enter the source filename: ")
destination=input("Enter the destination filename: ")
with open(starting,"r") as file1,open(destination,"w") as file2:
    for line in file1:
        file2.write(line)
        print("File copied successfully")

#3rd question
with open("test.txt","r") as file1:
    content=file1.read()
    words=content.split()
    word_number=len(words)
    print(word_number)

#4th question
try:
    string=input("Enter a string: ")
    num_string=int(string)
    print(f"The string is: {num_string}")
except Exception as e:
    print(f"Some error occured: {e}")    

#5th question
lists=[]
try:
    num1=int(input("Enter a list of integers: "))
    lists.append(num1)
    for i in lists:
        if i < 0:
            raise ValueError
    print("All are positive")
except Exception as e:
    print(f"Some error occured: {e}")
    
#6th question
try:
    num1=input("Enter few numbers: ")
    integer_list = [int(x) for x in num1.split()] #referred the internet for this line
    average=sum(integer_list)/ len(integer_list)
    print(f"The average of the numbers is: {average}")
except Exception as e:
    print(f"Some error occured: {e}")
finally:
    print("Code has been executed")    

#7th question
try:
    filename=input("Enter filename: ")
    message=input("Enter the message: ")
    with open(filename,"a") as file1:
        file1.write(message)
    print("Message has been written")    
except Exception as e:
    print(f"Some error occured: {e}")