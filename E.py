t = int(input())
for step in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    status = 'YES'
    a = []
    for i in range(n):
        if ai[i] in a:
            if ai[i] == ai[i-1]:
                a.append(ai[i])
            else:
                status = 'NO'
        else:
            a.append(ai[i])
    print(status)
