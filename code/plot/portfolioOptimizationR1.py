import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the expected returns and covariance matrix of your assets
returns = np.array([0.1, 0.2, 0.15])
covariance = np.array([[0.05, 0.02, 0.01], [0.02, 0.06, 0.03], [0.01, 0.03, 0.04]])

# Define a function to calculate the portfolio return and risk
def portfolio_return(weights, returns):
    return np.sum(weights * returns)

def portfolio_risk(weights, covariance):
    return np.sqrt(np.dot(weights.T, np.dot(covariance, weights)))

# Define a function to minimize the portfolio risk
def minimize_risk(weights, returns, covariance):
    return portfolio_risk(weights, covariance)

# Define the constraints for your optimization problem
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Define the bounds for your optimization problem
bounds = tuple((0, 1) for i in range(3))

# Define an initial guess for your optimization problem
guess = [1/3, 1/3, 1/3]

# Solve the optimization problem using scipy.optimize.minimize()
result = minimize(minimize_risk, guess, args=(returns,covariance), method='SLSQP', bounds=bounds, constraints=constraints)

# Print the optimal weights for each asset
print(result.x)
