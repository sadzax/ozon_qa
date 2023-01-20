def enter_int(arg_min=-10000000, arg_max=10000000, arg_not=None, input_description='', arg_error='error'):
    while True:
        try:
            i = int(input(input_description))
            if i < arg_min or i > arg_max or i == arg_not:
                print(arg_error)
                continue
            return i
        except:
            print(arg_error)
            continue


def enter_pair(input_description='', arg_error='error'):
    i = ''
    while True:
        try:
            i = str(input(input_description))
            if i.find(' ') == -1:
                print(arg_error)
                continue
            return i
        except:
            print(arg_error)
            continue


def sum_pair(string):
    a = int(string[:string.find(' ')])
    b = int(string[string.find(' ') + 1:])
    return int(a + b)


t = enter_int(1, 1000)
pairs = []
for step in range(t):
    pairs.append(enter_pair())

for a_pair in pairs:
    print(sum_pair(a_pair))
