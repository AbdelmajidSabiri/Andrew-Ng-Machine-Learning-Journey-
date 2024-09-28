import numpy as np


X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])

b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])


# Predict price of a single house (Normal For Loop)
def predict_single_loop(x, w, b): 

    n = x.shape[0]
    p = 0
    for i in range(n):
        p_i = x[i] * w[i]  
        p = p + p_i         
    p = p + b                
    return p


# Predict price of a single house (Using Vectorization)
def predict_single_vector(x,w,b) :
    return np.dot(x,w) + b

row1 = X_train[0,:]
print(f"Predict with normal loop : {predict_single_loop(row1,w_init,b_init)}\nPredict with Vectorization : {predict_single_vector(row1,w_init,b_init)}")
print("*"*30)


# Function do calculate Cost
def Cost(x,y,w,b) :
    m = x.shape[0]
    SumError = 0
    for i in range(m) :
        SumError = SumError + (predict_single_vector(x[i,:],w,b) - y[i])**2
    
    return SumError/(2*m)

cost = Cost(X_train, y_train, w_init, b_init)
print(f'Cost at optimal w : {cost}')

