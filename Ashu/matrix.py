# Matrix

row = int(input("Enter the number of row : "))
column = int(input("Enter the number of column : "))

matrix = []

print("Enter the matrix row wise : ")
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input("Enter Number : ")))
    matrix.append(a)

for Row in range(row):
    for Column in range(column):
        print(matrix[Row][Column], end = " ")
    print()    