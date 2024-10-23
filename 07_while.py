# while loop = a statement that will execute it's block of code,
#              as long as its condition remains true
# name=""
# while(len(name)==0):
#     name=input("what is your name")
# print("HELLO "+ name)
#another Way
name=None
while not name:
    name= input("Who are You?")
print("Welcome Mr."+name)