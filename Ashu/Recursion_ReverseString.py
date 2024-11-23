def ReverseString(s):
    if len(s) <= 1:
        return s
    else:
        return ReverseString(s[1:])+s[0]
s = input("Enter String : ")    
ReverseString(s)
print(f'{s} : {ReverseString(s)}')
