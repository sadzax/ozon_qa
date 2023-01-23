t = int(input())
for i in range(t):
    n = int(input())
    p = (input().split())
    p_dict = {}
    p_dict_discount = {}
    total = 0
    for el in p:
        p[p.index(el)] = int(el)
        p_dict[el] = p.count(int(el))
    for key in p_dict:
        discount = p_dict[key] // 3
        p_dict_discount[key] = p_dict[key]-int(discount)
        total = total + int(key) * p_dict_discount[key]
    print(total)