
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    s = input()
    t = input()
    memo = {}

    def dp(res):
        if s not in res and t not in res and len(res) == 3 * n:
            if 'a' in res and 'b' in res and 'c' in res:
                if res.count('a') == res.count('b') == res.count('c'):
                    return res
        if len(res) > 3 * n:
            return None
        if (res, s, t) in memo:
            return None

        updated_res = dp(res + 'a')
        if updated_res:
            return updated_res

        updated_res = dp(res + 'b')
        if updated_res:
            return updated_res

        updated_res = dp(res + 'c')
        if updated_res:
            return updated_res

    res = dp('')
    if res:
        print("YES")
        print(res)
    else:
        print("NO")
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
