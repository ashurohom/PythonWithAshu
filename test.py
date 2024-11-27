try:
    a=int(input("Enter Number 1 : "))
    b=int(input("Enter Number 2 : "))
    print(a/b)
    # print(a/c)
    l1 = [1,2,3]
    # print(l1[5])

    l1.append_new(4)

except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("Invalid Value")
except TypeError:
    print("Invalid DataType")    
except NameError:
    print("Name or Variable Not Fount")
except IndexError:
    print("Invalid Index Number")   
except AttributeError:
    print("Invalid attribute")         

finally:
    print("In Finally Block")    