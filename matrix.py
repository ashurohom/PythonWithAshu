row = int(input("Enter No Of Row : "))
column = int(input("Enter No Of Column : "))

matrix = []

print("Enter Number Row Wise : ")
for i in range(row):

    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)

for Row in range(row):
    for Column in range(column):
        print(matrix[Row][Column], end=" ")
    print()        


 