# Q1. Write a Python program that takes a person's age and categories it as:
#Child (<13)
#Teen (13–19)
#Adult (20–59)
#Senior (60+)

age=int(input("Enter your age:"))

if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")

    



# Q2. Write a Python program to check if a given number is positive, negative or zero .

num=int(input("Enter the Number:"))

if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")





# Q3. Write a Python program to:

# * Print the first and last item of a number list

list=["Ali", "Moiz", "Sara", "Saad", "Zara", "Zain"]

print("First item of a list:", list[0])
print("Last item of a list:", list[-5])

# * Print the number in the list

numbers =[10,20,30,40,50,60,70,80,90]
print("Number in the list:", len(numbers))




# Q4. Write a Python program to Create a Dictionary and then update its value

dict ={"Ali" : 1, 
       "Moiz" : 20,
        "Sara" : 30, 
        "Saad" : 40, 
        "Zara" : 50, 
        "Zain" : 60}
print("My Dictionary:", dict)

dict["Ali"] = 10
print("Updated Dictionary:", dict)
