import numpy as npy, matplotlib.pyplot as plt, math

def function_creator(x,n):
    out = 0
    while n:
        out += pow(x,n)*n
        n = n-1
    out = out-10
    return out


def bisection(a,b,polynomial_power,atol):
    fa = function_creator(a, polynomial_power)
    fb = function_creator(b, polynomial_power)

    if fa*fb >= 0:
        print("invalid input for bisection method")
        return

    if atol :
        iteration = math.log2((b-a)/(2*atol))

    elif atol == 0:
        iteration = 1

    while fa*fb < 0 and iteration:
        mid_point = (a+b)/2
        fmid = function_creator(mid_point,polynomial_power)
        if atol != 0:
            iteration = iteration-1
        if fmid*fa <= 0:
            b = mid_point
            fb = fmid
        if fmid*fb <= 0:
            a = mid_point
            fa = fmid
        if fa == 0 or fb == 0:
            if fa == 0:
                b = a
            else:
                a = b
    return (a+b)/2

first_result = bisection(0.0,10.0,4,0)
print(first_result)