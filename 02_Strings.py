name01 ="hitesh soni"
print("Hello this is Hitesh Soni ,\nand i want to change line by using \t escape sequance character")
#concatination of string
print("This is first string" + " " + "and this is my second string")
#printing name
print("printing name: ",name01)
#printing lenght of name01 variable 
print("printing lenght of name01 variable ",len(name01))
#indexing
print("indexing of name01[3]",name01[3])#output is "e"
#Finding any letter or group of words into the string, it will return the index where it will found
print("it will returns the index of starting of ' so': ",name01.find(" so"))
#capitalizing the first letter of string 
print("capitalizing the first letter of string :",name01.capitalize())
#This is used to convert string to upper case
print("This is used to convert string to upper case",name01.upper())
name02= "Tara Chand Soni"
#This is used to convert all letters to lower case of string 
print("This is used to convert all letters to lower case of string",name02.lower())
name03 = "123"
name04= "Hitesh0123"
#This is for checking is the string is totally digit or not
print("This is for checking is the string is totally digit or not: ",name03.isdigit())
print("This is for checking is the string is totally digit or not: ",name04.isdigit())
#this is to check space if there is any space it will return true
name05="hiteshsoni"
print("this is for counting characters in the given string: ",name05.isalpha())
#this is for counting characters in the given string
print("this is for counting characters in the given string: ",name02.count("a"))
#this is for replace any string or string part to another string or string part
print("this is for replace any string or string part to another string or string part: ",name05.replace("hitesh","tarachand"))
print(name05.endswith("soni"))#checks the string ends with "soni"
print(name05.count("i"))#counts the frequency of word "i"



#slicing
name="Hitesh Soni"
#slicing by inboxing index no. [start:stop:step/jump]
first_name= name[0:6]
print(first_name)
print(name[0:11:2])
#this is how we can reverse an string
print(name[::-1])
#slicing using slice function
website="http://www.google.com"
print(website[slice(11,-4)])
