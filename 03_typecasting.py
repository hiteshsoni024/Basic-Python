#type casting is to convert the data type of a value to another data type
x=3   #int
y=2.4 #float
z="6" #string

y=int(y) # y is converted into int datatype
z=float(z)#z is converted into float datatype
x=str(x) #x is converted into string datatype
print(x)
print(y)
print(z)
#taking input form user is always a string type data
name = input("What is your name?")
print("Hello "+name)
print(type(name))
#to operate sum operations on users input we have to type caste the data
age = int(input("How old are you?"))
#or
# age= int(age)
age+=1
print("you are "+str(age)+" years old")
print(type(age))

