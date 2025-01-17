# '''Conditional statement'''
# age=int(input("How old are you?"))
# if(age>=18 and age<100):
#     print("you are eligible for voting")
# elif(age<=0 or age>=100):#elif statement tabhi check hogi agr if statement false ho
#     print("please enter a valid age")
# else:
#     print("you are not eligible for voting")
# #logical operator
# # and
# # or
# # not(condition)

# #traffic system
# light = input("Enter the color of Traffic light : ");
# if(light=="red" or light == "RED" or light == "Red"):
#     print("Stop")
# elif(light=="Yellow" or light=="yellow" or light=="YELLOW" ):
#     print("Get Ready")
# elif(light=="Green" or light=="green" or light=="GREEN"):
#     print("Go")
# else:
#     print("Choose one from red, green, yellow")


# #grading system
# marks= int(input("Enter your marks: "))
# if ( marks >=90 and marks < 100):
#     print("grade: A")
# elif(marks<90 and marks>=80):
#     print("grade: B")
# elif(marks<80 and marks>=70):
#     print("grade: C")
# elif(marks<70 and marks > 35):
#     print("grade: D")
# elif(marks<35 and marks > 0):
#     print("faild")
# else:
#     print("Enter valid marks")

'''practice'''
# WAP to check if a number entered by the user is odd or even.
num = int(input("enter number: "))
if(num%2==0):
    print("even")
else:
    print("odd")

# WAP to find the greatest of 3 numbers entered by the user
num1=int(input("enter first num: "))
num2=int(input("enter second num: "))
num3=int(input("enter third num: "))
if(num1>=num2 and num1>=num3):
    print("num1 is greatest")
elif(num2>=num1 and num2>=num3):
    print("num2 is greatest")
elif(num3>=num1 and num3>=num2):
    print("num3 is greatest") 
    