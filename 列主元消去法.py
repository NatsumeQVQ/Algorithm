import numpy as np
import math
arr = np.array([[-3.,2.,6.,4.],[10.,-7.,0.,7.],[5.,-1.,5.,6.]])
for i in range(2):
    max = math.fabs(arr[i,i])
    for (index,k) in enumerate(arr[:,i]):
        if math.fabs(k)>=max:
            max_index = index+i
            max = math.fabs(k)
    arr[[i,max_index+i],:] = arr[[max_index+i,i],:]
    for (index,each) in enumerate(arr[i+1:]):
        arr[index+i+1] = each - each[i]*arr[i]/arr[i,i]
print(arr)
arr_reverse = list(arr)
arr_reverse.reverse()
arr_reverse = np.array(arr_reverse)
x = []
for (i,each) in enumerate(arr_reverse):
    for count in range(i):
        each[-1] = each[-1]-each[-2-count]*x[count]
    x.append(each[-1]/each[-2-i])
print(x)