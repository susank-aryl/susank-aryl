import numpy as np
import pandas as pd
import random

def linear_regression(x, w, b)-> np.ndarray:
    f_wb = np.dot(w,x) + b
    return f_wb


w = np.random.uniform(1,10)
b = random.uniform(1,10)
x = np.random.uniform(-5,5,size = 10)

print(linear_regression(w,b,x))


