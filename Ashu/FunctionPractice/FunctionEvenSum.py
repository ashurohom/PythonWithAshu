'''4. Implement a function that returns the sum of all even numbers between two given integers (inclusive).

Example:
Input: start=2, end=10
Output: 30 (2 + 4 + 6 + 8 + 10)
'''

def EvenSum():
    start=2
    end=10
    result=0

    for i in range(start,end+1):
        if i%2==0:
            result+=i
    print(result)
EvenSum()            