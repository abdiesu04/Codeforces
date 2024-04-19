n , m = map(int , input().split())
flag = True
prev_color = None
for _ in range(n):
    arr = list(input().strip())
    length = len(set(arr))
    if length != 1 or (prev_color is not None and prev_color == arr[0]):
        flag = False
        break
    prev_color = arr[0]

print("YES" if flag else "NO")