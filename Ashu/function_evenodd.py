# Odd even code using Function and store in List

list = [1,2,3,4,5,6,7,8,9,10]

def evenodd(list):
    even = []
    odd = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    print(f'Even Number : {even}')            
    print(f'Odd Number : {odd}')            
evenodd(list)