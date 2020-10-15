from math import *
print('x', 'y', sep='    ')
x = 1.0
while x <= 2:
    print(x, round(cos(2/x)-2*sin(1/x)+1/x, 2))
    x = round(x + 0.1, 1)
