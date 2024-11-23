# Using Function Remove the dublicate string and print string, store dublicate string in another variable 
# also count the dublicate string 


str = "progrramming"

def strings(str):
    new_str = " "
    dublicatevalue = " "
    dublicatecount = {}

    for i in str:
        
        if i not in new_str:            # If the character is not already in the new_str

            new_str += i                # Add the character to new_str
        
        else:                           # If the character is already in the new_str

            if i in dublicatecount:     # Check if the character is already in the dublicatecount dictionary

                dublicatecount[i] += 1  # If it is, increment its count by 1

            else:
                dublicatevalue += i + " "                 # If it isn't, add it to dublicatevalue with a space and initialize its count in dublicatecount as 2 (since it's a duplicate)

                dublicatecount[i] = 2   # Set count to 2 since it appears for the second time

    print(f'Original String : {str}')
    print(f'Without Dublicate : {new_str}')
    print(f'Dublicate Value : {dublicatevalue}')
    print(f'Dublicate Char and Count : {dublicatecount}')

strings(str)



'''
OutPut
Original String : progrramming
Without Dublicate :  progamin
Dublicate Value :  r m g 
Dublicate Char and Count : {'r': 3, 'm': 2, 'g': 2}
'''