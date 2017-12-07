import math
def newton(n):
    newton_iter = lambda x:x-(x**3-3*x-1)/(3*x**2-3)
    a = newton_iter(n)
    b = newton_iter(a)
    while math.fabs(b-a)>=0.005:
         a = b
         b = newton_iter(b)
         print(b)
    print(round(b,3))
newton(2)