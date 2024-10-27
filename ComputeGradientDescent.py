
def compute_gradient(x, y, w, b): 

    # Number of training examples
    m = x.shape[0]
    
    # You need to return the following variables correctly
    dj_dw = 0
    dj_db = 0
    
    ### START CODE HERE ###
    
    for i in range(m):
        
        prediction = w*x[i]+b

        dj_dw += (prediction - y[i]) * x[i]
        dj_db += (prediction - y[i])
    
    
    dj_dw = dj_dw/m
    dj_db = dj_db/m
    
    ### END CODE HERE ### 
        
    return dj_dw, dj_db