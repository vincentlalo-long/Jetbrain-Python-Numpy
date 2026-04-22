import numpy as np

a = np.array([['clear', 'usually', 'of'],
              ['conscience', 'the', 'bad'],
              ['is', 'sign', 'memory']])
a = a.T

b = np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]])
b = b.T

c = np.arange(12).reshape(3,2,2).transpose(2,1,0)


if __name__ == '__main__':
    print(a)
    print(b)
    print(c)

