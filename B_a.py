from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    counts = Counter(p)
    print(sum(x * (counts[x] - counts[x] // 3) for x in counts))
