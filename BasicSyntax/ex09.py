import statsmodels.api as sm
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [1.1, 2.1, 3.1, 4.1,5.1,6.1, 7.1, 8.1, 9.1, 10.1]

X = sm.add_constant(x)
# y = b0 + b1 * x
# lny = b0 + b1 * lnx

#x = np.log(x)
#y = np.log(y)


model = sm.OLS(y,X)
result_ols = model.fit()
print(result_ols.summary())

