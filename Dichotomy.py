import math
def dichotomy(min,max,r):
    fun = lambda x:x**3-x*2-5
    fun_min = fun(min)
    fun_max = fun(max)
    if fun_min*fun_max<0:
        if fun_max:
            pos = max
            nag = min
        else:
            pos = min
            nag = max
        n = 1
        while True:
            n += 1
            center = (pos + nag)/2
            fun_cen = fun(center)
            if math.fabs(pos - nag)<r:
                print((max-min)/2**n)
                return round(center,4)
            if fun_cen>0:
                pos = center
            else:
                nag = center

print(dichotomy(2,3,0.0001))
