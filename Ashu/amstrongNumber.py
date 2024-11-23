# 153 = 1**3, 5**3. 3**3 = 153

number = int(input("Enter Number : "))

digit=[int(d) for d in str(number)]

l = len(digit)

armstrong = sum(d ** l for d in digit)

if number == armstrong:
    print("The", number, "Is Armstrong Number")
    print(f'The {number} Is Armstrong Number')
else:
    print(f'{number} Is Not Armstrong Number')    