import random
import numpy as np

print("With seed:")
random.seed(42)
print(random.random())
rng = np.random.default_rng(42)
print(rng.random())
