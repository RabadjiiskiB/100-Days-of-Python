nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
N = input()
number = 0
for s in N:
    if s in nums:
        number += int(s)
N = number
while N > 9:
    number = 0
    for s in str(N):
        if s in nums:
            number += int(s)
    N = number

print(N)
