import random
import numpy as np

#Edit to trigger
print("Edit")
# Without setting a seed (results will vary each run)
print("Without seed:")
print(random.random())
print(random.randint(1, 10))

rng = np.random.default_rng()

print(rng.random())
