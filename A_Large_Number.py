t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    number = input()

    leftmost = -1
    for i, digit in enumerate(number):
        if int(digit) < d:
            leftmost = i
            break
    
    if leftmost == -1:
        number += str(d)
    else:
        number = number[:leftmost] + str(d) + number[leftmost:]
    
    print(number)