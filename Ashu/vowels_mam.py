str = 'aeiou'

# str1 = input("Enter String : ").strip().lower()
# count=0
# for i in str1:
#     if i in str:
#         count+=1

# print(f'No Of Vowels : {count}')        

# str1 = input("Enter String : ")
# print(f"Length : {len(str1)}")

# l=0
# for i in str1:
#     l+=1
# print(f'lengthl : {l}')     


str3 = input("Enter String : ")

d={}
for i in str3:
    d[i] = str3.count(i)
print(f'lengthl : {d}')   