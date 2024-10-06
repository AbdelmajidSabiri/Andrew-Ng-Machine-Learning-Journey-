import numpy as np
import matplotlib.pyplot as plt


X_train = np.array([[952, 2, 1, 65], [1244, 3, 2, 64], [1947, 3, 2, 17]])
Y_train = np.array([271.5,232,509.8])

X_features = ['size(sqft)','bedrooms','floors','age']

fig,ax=plt.subplots(1, 4, figsize=(12, 3), sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:,i],Y_train)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel("Price (1000's)")
plt.show()


def zscore_normalize_features(X):

    mu     = np.mean(X, axis=0) 
    sigma  = np.std(X, axis=0)

    X_norm = (X - mu) / sigma      
    return (X_norm, mu, sigma)
 

def normalize(x_house, X_mu, X_sigma) :

    x_house_norm = (x_house - X_mu) / X_sigma
    return x_house_norm