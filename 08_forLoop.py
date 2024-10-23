# for loop= a statement that will execute it's block of code a limited amount of time
#     while loop = unlimited
#     for loop = limited

for i in range(10):
    print(i+1)
    print("hello everyone")  
#here in range (start, end, gap)
for i in range(50,60+1,2):
    print(i)
#we can also set range as a string
for i in "Hitesh Soni":
    print(i)

#seting timer
import time
for second in range(10,0,-1):
    print(second)
    time.sleep(1)
print("HAPPY BIRTHDAY !")

#nested loop
rows= int(input("enter the no. of rows"))
columns= int(input("enter the no. of columns"))
symbol= input("enter any required symbol:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
print()