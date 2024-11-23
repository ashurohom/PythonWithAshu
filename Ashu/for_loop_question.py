'''1) Sum of a List: Write a program that calculates the sum of all the numbers in a list. 
    For example, given the list [1, 2, 3, 4, 5], the output should be 15'''

list = [1,2,3,4,5]

sum = 0
for i in list:
    sum = sum + i
print("Sum Of List : ",sum)
print("\n")    



'''2) Multiplication Table: Create a program that prints the multiplication table for a given number (e.g., 5). 
The output should show the results from 1 to 10. 
For example:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50'''


table = 5

for j in range(1,11):
    new_table = table * j
    print(table," * ",j," = ",new_table)



'''3) Count Vowels: Write a program that counts the number of vowels in a given string. For example, 
in the string "hello world", the output should be 3.'''

string = "Ashutosh"
vowels = "aeiouAEIOU"
count = 0
for a in string:
    if a in vowels:
        count += 1   #count = count + 1
print("vowels : ",count)    




'''4) Find Even Numbers: Create a program that prints all the even numbers between 1 and 50.'''


for num in range(1,51):
    if num % 2 == 0:
        print(num,end=" ")
    else:
        pass    




'''5) Reverse a String: Write a program that takes a string and prints it in reverse using a for loop. 
For example, for the input "hello", the output should be "olleh".'''

print("\n")
input = "hello"
print("String : ",input)

for c in reversed(input):
    print("",c,end=" ")



# 6) Deepak Problem Statement
# given list print all the element but list can start with index[2]
# Ex: list = [1,2,3,4,5]    output = [3,4,5,1,2]

print("\n")
my_list = [1,2,3,4,5]
start_index = 2
rotat_value = my_list[start_index:] + my_list[:start_index]
print(rotat_value,end=" ")

# Output : [3,4,5,1,2]


'''7)Count Specific Characters: Given a string, write a program that counts how many times the 
letter "a" appears in the string. For example, for the string "banana", the output should be 3.'''

print("\n")
strings = "banana"
count = 0

for e in strings:
    if e == 'a':
        count += 1
    else:
        pass
print("a = ",count)    



'''8) you have given a list, you can find all even number from that list and create a new list and insert 
all even number on that list'''

print("\n")
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_list = []
odd_list = []


for f in mylist:
    if f % 2 == 0:
        even_list.append(f)
    else:
        odd_list.append(f)
print(mylist)        
print("Even List : ",even_list)    
print("Odd List  : ",odd_list)    



'''9) Create a List of Squares: Write a program that generates a list of squares for the numbers from 1 to 10. 
      The output should be: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].'''

print("\n")
num_list = [1,2,3,4,5,6,7,8,9,10]
sq = []                     # value = []
for g in num_list:
    sq.append(g * g)       # value.append(sq)
print(sq)                  # print(value)



'''10) Fibonacci Sequence: Using a for loop, generate the first 10 numbers of the Fibonacci sequence. 
    The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. 
    The output should be: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].'''

print("\n")

f1 = 0
f2 = 1
f3 = []

for _ in range(10):
    f3.append(f1)                                # F(n) = F(n-1) + F(n-2)

    f1, f2 = f2, f1 + f2
print(f3)    


# OR

a,b = 0,1
d = [] 
d.append(a)
d.append(b)
for _ in range(8):
    c = a + b
    d.append(c)

    a=b
    b=c

print(d)