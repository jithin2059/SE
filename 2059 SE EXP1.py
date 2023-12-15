import numpy as np
import pandas as pd

def quadratic(coefficients):
    results = []
    for coeff in coefficients:
        a, b, c = coeff
        det = b**2 - 4*a*c
        if det < 0:
            results.append(None) 
        else:
            x1 = (-b + det**0.5) / (2*a)
            x2 = (-b - det**0.5) / (2*a)
            results.append((x1, x2))
    return results
singleset = np.array([[1, -3, 2]])
print(quadratic(singleset))

def dimarr():
    singleset = np.array([[1, -3, 2]])
    
    mulset = np.array([
        [1, -3, 2],
        [2, 5, -3],
        [1, 0, -1]
    ])
    
    return quadratic(singleset),quadratic(mulset)
dimarr()

def hardcoding():
    abc=[(1,-3,2)]
    return quadratic(abc)
result = hardcoding()
print(result)

def inputvar():
    lst = []
    x = int(input('a: '))
    y = int(input('b: '))
    z = int(input('c: '))

    lst.extend([(x, y, z)])
    
    return quadratic(lst)
inputvar()

def file():
    df = pd.read_csv('coeff.csv')
    a = df['a'][0]
    b = df['b'][0]
    c = df['c'][0]
    arr = pd.array([[a,b,c]])
    return quadratic(arr)
file()

import matplotlib.pyplot as plt
def quadratic_solution(a, b, c, x):
    y = a * x**2 + b * x + c
    return y
def temptime(a, b, c, time_line):
    time = np.array(time_line)
    temperature = quadratic_solution(a, b, c, time)

    plt.plot(time, temperature)
    plt.title("Temp")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.show()
def show():
    p = int(input("a:"))
    q = int(input("b:"))
    r = int(input("c:"))
    
    time_line = np.linspace(0, 5, 10)
    

    temptime(p,q,r, time_line)
    
show()
