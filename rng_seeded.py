import random
import numpy as np

print("Without seed:")
print(random.random())
print(random.randint(1, 10))

rng = np.random.default_rng(42)

print(rng.random())
