t = int(input())
for _ in range(t):
    n = int(input())
    arr  = list(map(int , input().split()))
    def merge(l , r , arr):
        if l == r:
            return [arr[l]]
        mid = l + ( r- l) // 2
        lh = merge(l , mid , arr)
        rh = merge(mid+ 1 , r , arr)
        i , j = 0 , 0 
        k = 0
        res = []
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                res.append(lh[i])
                i += 1
            else:
                res.append(rh[j])
                
                j += 1
            k += 1
        res[k:] = lh[i:] if i < len(lh) else rh[j:]
            
