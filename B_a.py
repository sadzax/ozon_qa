t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    p_set = list(set(p))
    print(sum(map(lambda x: x * (p.count(x) - p.count(x) // 3), p_set)))
