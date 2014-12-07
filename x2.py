import numpy as np
import matplotlib.pyplot as plt

trX = np.linspace(-5, 5, 101)
trY = trX ** 2 + np.random.randn(*trX.shape) * 1.3 # noise for training

# plt.plot(trY, '.')
# plt.show()

teX = np.linspace(-7, 7, 101)
teY = teX ** 2 # no noise for testing