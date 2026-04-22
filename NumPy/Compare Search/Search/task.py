import numpy as np
rng = np.random.default_rng()

temperatures = rng.integers(25, size=7)
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
condition = temperatures > 15
high = "High"
low = "Low"
result = np.where(condition,high,low)
warm_days = days[condition]

if __name__ == '__main__':
    print(temperatures)
    print(result)
    print(warm_days)


