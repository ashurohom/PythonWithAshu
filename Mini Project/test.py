dict = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
}

print(dict)
print(dict.items())

for menu, order in dict.items():
    print(f'{menu} : {order} Rs.')