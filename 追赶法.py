import numpy as np
A = np.array([[2.,1.,0,0],[1.,3.,1.,0],[0,1.,1.,1.],[0,0,2.,1.]])
d = [1.,2.,-2.,0.]
L = np.zeros((4,4))
U = np.eye(4)
L[0,0] = A[0,0]
for (index,each) in enumerate(A[1:,]):
    U[index,index+1] = A[index,index+1]/L[index,index]
    L[index+1,index] = each[index]
    L[index+1,index+1] = each[index+1]-each[index]*U[index,index+1]
y = [d[0]/L[0,0]]
for (index,each) in enumerate(L[1:,]):
    y.append((d[index+1]-each[index]*y[index])/each[index+1])
print(y)
y.reverse()
arr_reverse = list(U)
arr_reverse.reverse()
arr_reverse = np.array(arr_reverse)
x = [y[0]/arr_reverse[0,-1]]
for (index,each) in enumerate(arr_reverse[1:,]):
    x.append((y[index+1]-each[-index-1]*y[index])/each[-index-2])
print(L,'\n',U)
print(x)