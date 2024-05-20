# test_cases=int(input())
# while(test_cases>0):
#     n=int(input())
#     cards=input().split(' ')
#     new_deck=[]
#     while(len(cards)>0):
#         max_index=cards.index(max(cards))
#         new_deck+=cards[max_index::]
#         cards=cards[0:max_index]
#     print(*new_deck,sep=' ')  
#     print('')
#     test_cases-=1

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int , input().split()))
    res  = []
    while len(p) > 0:
        mx_idx  = p.index(max(p))
        res+=(p[mx_idx::])
        p = p[0:mx_idx]
    print(*res)
			