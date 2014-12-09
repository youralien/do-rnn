import numpy as np
import matplotlib.pyplot as plt

trX = np.linspace(-5, 5, 101)
trY = trX ** 2 + np.random.randn(*trX.shape) * 1.3 # noise for training


teX = np.linspace(-7, 7, 101)
teY = teX ** 2 # no noise for testing

plt.hold('on')
plt.plot(trX, trY, 'r.')
plt.plot(teX, teY, 'b-')
plt.show()

tru = trX.reshape(-1, 1)
trt = trY.reshape(-1, 1)
teu = teX.reshape(-1, 1)
tet = teX.reshape(-1, 1)

print tru.shape

