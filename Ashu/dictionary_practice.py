mydict = {
    "Name" : "Ashu",
    "Village" : "JK",
    "Taluka" : "Kopargaon",
    "District" : "Ahilyanagar",
    "State" : "Maharashtra",
    "City" : "Kopargaon"
}

# Print
print()
print(mydict)  

# datatype nd length
print()
print("Type : ",type(mydict),"Length : ",len(mydict))

# accessing value using key name
print()
print(mydict["Taluka"])

# update value
print()
mydict["Name"]="Ashitosh"
print(mydict)

# delete key value pair
print()
del mydict["City"]
print(mydict)

# clear/empty the dictionary
# mydict.clear()
# print(mydict)   #empty dictionary

# create dictionary using object
print()
newdict = dict()
print(type(newdict))    #<class 'dict'>

# newdict2 = eval(input("Enter New Dictionary : "))
# print(type(newdict2),newdict2)
#negative value acceptedd in dictionary



# nested dictionary
print()

student = {
    "Name" : "Ashu",
    "RollNo" : "111",
    "Marks" : {
        "First Year" : "85",
        "Second Year" : "92",
        "Third Year" : "70",
        "Final Year" : "81",},
    "College" : "Sanjivani COE",
}

print(student["Marks"]["Final Year"])



# get
print()
print(student.get("Names")) #None


# pop
print()
# print(student.pop("RollNo"))    #111

#popitem : remove last element in new latest version(Pyton 3.7)
print()
# print(student.popitem()) 
# print(student.popitem())
# print(student.popitem())


# keys
print()
print(student.keys())

# values
print()
print(student.values())

# Items : tuple
print()
print(student.items())

# copy
print()
d = student.copy()
print(d)

# dictionary comprehension
print()
a = {x:x**2 for x in range(1,6)}
print(a)

print(student.keys())
print(student.get["Name"])
