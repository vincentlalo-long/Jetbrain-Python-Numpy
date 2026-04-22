import numpy as np

x = np.arange(35)
y = x.reshape(5, 7)

a = x[[7,13,28,33]]
b = x[[[0,1,2],[10,11,12],[28,29,30]]]


c = y[[0,2,4]]
d = y[[0,2,4],[0,1,2]]
e = y[[1,2,4],6]


if __name__ == '__main__':
    print(y)
    print('\n', a.shape)
    print('\n', b.shape)
    print('\n', c.shape)
    print('\n', d.shape)
    print('\n', e.shape)
