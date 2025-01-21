'''VARIABLES AND TYPECASTING'''
'''LECTURE 01'''
'''VARIABLES'''
# First_name= "hitesh"
# last_name= "soni"
# #these are strings
# print("Hello"+" " + First_name+" "+last_name)
# print(type(First_name))

# age = 12
# #here age is int data type
# number = "12"
# #here number is str data type
# age += 1 #here we are increase age by 1
# print("your age is :"+ str(age))
# #we can only concatinate string data with only string 
# print(number)
# height= 250.6
# #this is float data type
# print("your height is :"+str(height)+"cm")
# human=True
# #this is boolean data type
# print(type(human))
# print("Are you a human: "+str(human))

# #multipple assignment 
# name,weight,standard= "Hitesh", 83, "A"
# print(name)
# print(weight)
# print(standard)
'''TYPECASTING'''
#type casting is to convert the data type of a value to another data type
# x=3   #int
# y=2.4 #float
# z="6" #string

# y=int(y) # y is converted into int datatype
# z=float(z)#z is converted into float datatype
# x=str(x) #x is converted into string datatype
# print(x)
# print(y)
# print(z)
# #taking input form user is always a string type data
# name = input("What is your name?")
# print("Hello "+name)
# print(type(name))
# #to operate sum operations on users input we have to type caste the data
# age = int(input("How old are you?"))
# #or
# # age= int(age)
# age+=1
# print("you are "+str(age)+" years old")
# print(type(age))



'''PRACTICE OF LECTURE 01'''
#Write a Program to input 2 numbers & print their sum.
a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
print(a+b)

# WAP to input side of a square & print its area
x= int(input("Enter the one side of a rectangle/square: "))
y= int(input("Enter another side of a rectangle/square: "))
print("The area of rectangle/square: ", x*y)

#WAP to input 2 floating point numbers & print their average
A= float(input("Enter the first num: "))
B= float(input("enter the second num: "))
print("the avg is : ", float((A+B)/2))

# WAP to input 2 int numbers, a and b. 
# Print True if a is greater than or equal to b. If not print False
X=int(input("Enter first num: "))
Y= int(input("Enter second num: "))
print(bool(a>=b))