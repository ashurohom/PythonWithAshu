
z={
    "sql":80,
    "web":78,
    "python":50
}
# print(z)
sum=0
for i in z:
    sum+=z[i]
print(sum)    



s=0
l=len(z)
for j in z.values():
    s+=j
    
print(s/l)