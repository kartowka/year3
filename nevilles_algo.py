"""
A Python program for the Neville's algorithm.
Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
"""

__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"

def neville(datax, datay, x):
    """
    Finds an interpolated value using Neville's algorithm.
    Input
      datax: input x's in a list of size n
      datay: input y's in a list of size n
      x: the x value used for interpolation
    Output
      p[0]: the polynomial of degree n
    """
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
    return p[0]

datax = [1.2,1.3,1.4,1.5,1.6]
datay = [3.5095,3.6984,3.9043,4.1293,4.3756]
x = 1.37

print(neville(datax,datay,x))

def nevilleInter(points, x):
    """
    :param points: a list of points ie ((0,1),(1,2)) etc..
    :param x: the x in question of what the value is at this x
    :return: the value y at the given x
    """
    if len(points) < 2:
        return "Invalid points"

    p = [[0 for j in range(len(points))] for y in range(len(points))]
    for i in range(len(points)):
        p[i][i] = points[i][1]
        if i + 1 < len(points):
            if points[i + 1][0] <= points[i][0]:
                return "Invalid points"
    i = 0
    j = 1
    t = j
    while True:
        print("P{0},{1}=(({2} - x{1}) * p{0}{3} - ({2} -x{0}) * p{4}{1}/ (x{0} - x{1})=".format(i,j,x,j-1,i+1),end="")
        p[i][j] = ((x - points[j][0]) * p[i][j - 1] - (x - points[i][0]) * p[i + 1][j]) / (
            points[i][0] - points[j][0])
        print(p[i][j])
        if i == 0 and j == len(points) - 1:
            break
        if j == len(points) - 1:
            i = 0
            j = t + 1
            t = j
        else:
            i += 1
            j += 1
    return p[0][-1]


print(nevilleInter(((1.2, 3.5095 ), (1.3, 3.6984), (1.4, 3.9043), (1.5, 4.1293),(1.6, 4.3756)),1.37))

