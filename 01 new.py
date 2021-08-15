import math

count = 0
user = input("exit")

while True:
    number = int(input("please enter your number:"))
    count = count + number
    print(count + number)


    if user == "exit":
        print("are you sure?")
        if user == "+":
            break
        if user == "-":
            print(count + number)