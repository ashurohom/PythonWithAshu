try:
    a=int(input("Enter Number 1 : "))
    b=int(input("Enter Number 2 : "))
    c=a/b
    print(c)

except ZeroDivisionError:
    print("Invalid Value Zero")    

except ValueError:
    print("Invalid Value")

except TypeError:
   print("Invalid Type")    

else:
    print("insid else")

finally:
    print("Always Print")

    
