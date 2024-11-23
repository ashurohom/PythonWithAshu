# given list find odd even and store it in a variable, variable not a list.


number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def oddeven(number):
    
    even = " "
    odd = " "
    for i in number:
        if i % 2 == 0:
            even+=str(i)
        else:
            odd+=str(i)    
    print(f'Even Number : {even}')            
    print(f'Odd Number : {odd}')

oddeven(number)

