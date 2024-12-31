# a=1234

# a=(str(a)[::-1])
# print(int(a))


def ReverseString(s):
    if len(s) <= 1:
        return s
    else:
        return ReverseString(s[1:])+s[0]
s = input("Enter number : "))    
ReverseString(s)
print(f'{s} : {ReverseString(s)}')
