

n_arr = int(input())
arr = []
lt = 0
rt = 0

for i in range(n_arr):
    l , r = map(int, input().split())
    lt += l
    rt += r
    arr.append([l, r])

res = abs(lt - rt)
mx = res
mxx = 0

for k in range(len(arr)):
    lk, rk = lt, rt
    lk += (arr[k][1] - arr[k][0])
    rk += (arr[k][0] - arr[k][1])
    if abs(lk - rk) > mx:
        mx = abs(lk - rk)
        mxx = k + 1
    
print(mxx)

				  	     	 		  			  			   		