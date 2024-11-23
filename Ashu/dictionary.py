# dictionary
# key value pair
# unordered, mutable, dublicate key  are not allowed
'''
key :  key can integer,float and string or tuple(tuple is immutable)
value : value can be anything integer,string,float,list,tuple etc...

ubordered : so indecing not allowed





# '''

dict = {
     "name" : "Ashitosh",
     "age" : 24,
     "class" : "B.tech",
     "marks" : 85,
     "Subject" : ['html','css','javascript','python'],
     "number" : (1,2,3,4,5)
}

 print(dict)
 print(len(dict))
 print(type(dict))

 print(dict["name"])
 print(dict["Subject"])

 dict["name"] = "AshuRohom"
 print(dict)

 # add new value

 dict["surname"] = "Rohom"
 print(dict)




 # nested dictionary

cardict = {
    'country' : 'india',
    'company' : 'mahindra',
    'vehicle' : {
        'bolero' : 5,
        '3xo' : 7,
        '7oo' : 4
        },
    'rank' : '2nd'     
}

print(cardict)
print(cardict['vehicle']['bolero'])





# methods in dictionary

# keys : return all keys
print(cardict.keys()) 

# values : return all values
print(cardict.values())
print(list(cardict.values()))

# items : return all (key, value) pairs as tuple

print(cardict.items())


# typecast

pairs = list(cardict.items())
print(pairs[0 ])

# key

print(cardict['country'])       #india
print(cardict.get('country'))   #india

# print(cardict['country2'])       #error
print(cardict.get('country2'))   #none

#update

cardict2 = {'price' : 1254221,}
cardict.update(cardict2)
print(cardict)