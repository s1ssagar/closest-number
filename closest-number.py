import math
tc = input()
while tc > 0:
    a, b, x = map(int, raw_input().strip().split(' '))
    num = math.pow(a, b)
    r = num % x
    if x % 2 == 0 and r <= x/2:
        print int(num - r)
    elif x % 2 == 0 and r > x/2:
        print int(num + (x-r))
    elif x % 2 == 1 and r < (x+1)/2:
        print int(num - r)
    elif x % 2 == 1 and r >= (x+1)/2:
        print int(num + (x-r))
    tc -= 1