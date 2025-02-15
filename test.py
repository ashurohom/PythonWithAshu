num = 11

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("No Prime Number")
            break
    else:
        print("Prime Number")    
else:
    print("No Prime Number")    