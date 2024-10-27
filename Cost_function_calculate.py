
def compute_cost(x, y, w, b): 

    m = x.shape[0] 
    total_cost = 0
    
    for i in range (m) :

        prediction = w*x[i] + b
        total_cost += (prediction - y[i]) ** 2
        
    total_cost = total_cost/(2*m)
    
    return total_cost