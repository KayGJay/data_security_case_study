import random
import numpy as np

print("Without seed:")
print(random.random())
rng = np.random.default_rng()
print(rng.random())
