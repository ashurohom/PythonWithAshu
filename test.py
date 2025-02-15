#1 Check Prime Number
#2 Find Factorial
#3 Print Prime number Between 1 TO 25
#4 Find Lowest and Second Lowest Number From Given List
#5 Find Highest And Second Highest Number From Given List
#6 Armstrong Number
#7 Find Length Of String With And Without len() Function
#8 WAP For Print Fibonacci Series
#9 Swap Two Number With or Without Third Variable
#10 Convert Number into its Corresponding String [1:one]


dict = {
    0 : "Zero",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
}

# num = int(input("Enter Number : "))
# print(f'{num} : {dict[num]}')

num =input("Enter Number : ")
output = " ".join(dict[int(digit)] for digit in num)
print(f'{num} : {output}')

