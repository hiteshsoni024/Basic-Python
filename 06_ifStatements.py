age=int(input("How old are you?"))
if(age>=18 and age<100):
    print("you are eligible for voting")
elif(age<=0 or age>=100):
    print("please enter a valid age")
else:
    print("you are not eligible for voting")
#logical operator
# and
# or
# not(condition)