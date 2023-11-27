import time
import numpy as np

a = np.random.randn(10000, 10000).astype(np.float32)
b = np.random.randn(10000, 10000).astype(np.float32)

start_time = time.time()
test = np.matmul(a, b)

print("----- %s seconds -----" % (time.time() - start_time))
