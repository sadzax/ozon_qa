from datetime import datetime


def check(enter, start, end, answer):
    if start <= enter <= end:
        return 'NO'
    else:
        return answer


t = int(input())
for step in range(t):
    n = int(input())
    stack = []
    answer = 'YES'
    for i in range(n):
        a, b = map(str, input().split("-"))
        if answer == "NO":
            pass
        else:
            try:
                a = datetime.strptime(a, '%H:%M:%S').time()
                b = datetime.strptime(b, '%H:%M:%S').time()
            except:
                answer = 'NO'
            try:
                if a > b:
                    answer = 'NO'
            except:
                pass
            if len(stack) > 0:
                for el in stack:
                    answer = check(a, el[0], el[1], answer)
                    answer = check(b, el[0], el[1], answer)
            stack.append([a, b])
    print(answer)
