import numpy as np


a = np.zeros((3, 4), dtype=np.int64)
b = np.array([[0,1,2,3]])
c = np.concatenate((a,b),axis = 0)

row1 = np.arange(10)
row2 = np.arange(20,30)
row3 = np.arange(40,50)
stacked = np.stack((row1 , row2 , row3), axis = 0)

if __name__ == '__main__':
    print(c)
    print(stacked)
