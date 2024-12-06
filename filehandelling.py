# f = open("notes.txt",'w+')
# print(f'file {f} created')
# f.close()


f1 = open('newnotes.txt','w+')
f1.write("Python Programming")
print(f'Position : {f1.tell()}')
f1.close()

l = ["\nAshitosh","Rohom"]
with open('newnotes.txt','a+') as file:
    file.seek(5)
    print(f'NewPosition : {file.tell()}')
    file.writelines(l)

l = ["\nBatch : P432","\nAddress : FC Road Pune"]
with open('newnotes.txt','a+') as file:
    print("File Added..")
    file.writelines(l)
