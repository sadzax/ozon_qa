from datetime import datetime


def check(left, right, start, end, ans):
    if start <= left <= end or start <= right <= end:
        return 'NO'
    elif start >= left <= end <= right >= start:
        return 'NO'
    else:
        return ans


def to_time(str1):
    return datetime.strptime(str1, '%H:%M:%S').time()


t = int(input())
for step in range(t):
    n = int(input())
    stack = []
    answer = 'YES'
    for i in range(n):
        a, b = map(str, input().split("-"))
        if answer != "NO":
            try:
                a = to_time(a)
                b = to_time(b)
                if a > b:
                    answer = 'NO'
                if len(stack) > 0:
                    #  version #1
                    # result = list(filter(lambda x: x[0] <= a <= x[1] or x[0] <= b <= x[1] or x[0] >= a <= x[1] <= b >= x[0], stack))
                    # if len(result) > 0:
                    #     answer = 'NO'
                    #  version #2
                    for el in stack:
                        answer = check(a, b, el[0], el[1], answer)
                stack.append([a, b])
            except:
                answer = 'NO'
    print(answer)
