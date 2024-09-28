import numpy as np
import time

def my_dot(w,b) :
    x=0
    for i in range(w.shape[0]):
        x = x + w[i] * b[i]
    return x

np.random.seed(1)
a = np.random.rand(10000000)  # very large arrays in order to make the diffrence important
b = np.random.rand(10000000)

tic = time.time()  # capture start time
c = np.dot(a, b)
toc = time.time()  # capture end time

print(f"np.dot(a, b) =  {c:.4f}")
print(f"Vectorized version duration: {1000*(toc-tic):.4f} ms ")

tic = time.time()  # capture start time
c = my_dot(a,b)
toc = time.time()  # capture end time

print(f"my_dot(a, b) =  {c:.4f}")
print(f"loop version duration: {1000*(toc-tic):.4f} ms ")

del(a);del(b)  #remove these big arrays from memory