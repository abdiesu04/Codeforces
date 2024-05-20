import sys, threading

def backtrack(arr, index,memo):
   
    if index >= len(arr):
        return 0
    to_go = arr[index] + index+1
    if index not in memo:
        memo[index] = ((to_go-1)- (index)) + backtrack(arr, to_go-1, memo)
    return memo[index]



t = int(input())
maxim = 0
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxim = float("-inf")
    for i in range(len(arr)):
        result = backtrack(arr, i, {})
        # print(result)
        if result > maxim:
            maxim = result
    print(maxim)
    


    
if __name__ == "backtrack":
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=backtrack)
    main_thread.start()
    main_thread.join()