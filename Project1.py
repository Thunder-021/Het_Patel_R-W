print("Welcome To the Intrective Personal Data Collecter!")

name=str(input("Please enter your Name : "))
age=int(input("Please enter your Age : "))
height=float(input("Please enter your height in meters : "))
favnum=int(input("Please enter your favourite number : "))

print("Thank you! Here is the information we collected:")

print("Name :",(name),type(name),"Memory address:",id(name))
print("age :",(age),type(age),"Memory address:",id(age))
print("Height :",(height),type(height),"Memory address:",id(height))
print("Name :",(favnum),type(favnum),"Memory address:",id(favnum))

year=2025-age
print("Your birth year is approximately: ",(year),"(Based on Your age of )",(age))
