def solve(l , r , arr):
    if r - l == 1:
        return 0
    mid = l + (r  - l ) // 2

    left_max = max(arr[l:mid])
    right_max = max(arr[mid:r])
    ans = 0
    if left_max > right_max:
        ans += 1
        arr[l:mid] , arr[mid:r] = arr[mid:r] , arr[l:mid]
    return solve(l, mid, arr) + solve(mid, r, arr) + ans


def solve_case(arr):
    ans = solve(0, len(arr), arr)
    if arr == sorted(arr):
        return ans
    return -1

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    print(solve_case(arr))