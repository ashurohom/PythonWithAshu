# wap to check number is armstrong or not
# 153 = (1)^3  (5)^3  (3)^3
#          1  +  125 + 27
#                153

# Armstrong Number = 153, 370, 371, 407

n=int(input("Enter A Number : "))
b = n
m = str(n)
k = len(m)
d = 0
while b > 0:
    c = b % 10
    c = c**k
    d += c
    b = b // 10
if d == n:
    print("It is armstrong number")    
else:
        print("It is not armstrong number")        


        