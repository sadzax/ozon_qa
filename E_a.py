a = []
for _ in range(10):
    i = input(int())
    if i in a:
        print('NO')
        break
    else:
        a.append(i)
