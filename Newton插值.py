import pandas as pd
import numpy as np
dq = pd.DataFrame({
    'x':np.array([1.615,1.624,1.702,1.828,1.921]),
    '0':np.array([2.4145,2.46459,2.65271,3.03035,3.34066]),
    '1':np.nan,
    '2':np.nan,
    '3':np.nan,
    '4':np.nan
})
x = 1.682
sum = 1
for column in range(4):
    for row in range(column,4):
        dq.iloc[row+1,column+1] = (dq.iloc[row,column]-dq.iloc[row+1,column])/(dq.iloc[row,5]-dq.iloc[row+1,5])
print(dq)
result = dq.iloc[0,0]
for i in range(4):
    for j in range(i+1):
        sum = sum*(x-dq.iloc[i,5])
    result = result +sum*dq.iloc[i+1,i+1]
print('result = ',result)