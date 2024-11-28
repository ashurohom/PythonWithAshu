def summ(num):
    if num < 10:
        return num
    else:
        return num%10 + summ(num//10)

print(summ(12345))

x = lambda a:a*a
print(x(2))