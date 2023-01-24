t = int(input())
for i in range(t):
    n = int(input())
    p = input().split()
    p_set = list(set(p))
    total = 0
    for el in p_set:
        count = p.count(el)
        discount = count // 3
        total = total + int(el) * (count - count // 3)
    print(total)
