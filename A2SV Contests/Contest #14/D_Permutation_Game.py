def solve():
    n, k, pb, ps = map(int, input().split())
    pb -= 1
    ps -= 1
    p = list(map(lambda x: int(x) - 1, input().split()))
    a = list(map(int, input().split()))

    b, s = [], []
    vb, vs = [False] * n, [False] * n

    while not vb[pb]:
        b.append(a[pb])
        vb[pb] = True
        pb = p[pb]

    while not vs[ps]:
        s.append(a[ps])
        vs[ps] = True
        ps = p[ps]

    sb, sc, csb, csc = 0, 0, 0, 0
    for i in range(min(len(b), k)):
        sb = max(sb, csb + b[i] * (k - i))
        csb += b[i]

    for i in range(min(len(s), k)):
        sc = max(sc, csc + s[i] * (k - i))
        csc += s[i]

    print("Draw" if sb == sc else "Bodya" if sb > sc else "Sasha")


test_cases = int(input())
for _ in range(test_cases):
    solve()
