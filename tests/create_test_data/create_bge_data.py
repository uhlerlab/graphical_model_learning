from graphical_models.rand import directed_erdos, rand_weights
import numpy as np
import random
import os
np.random.seed(12312)
random.seed(12312)

d = directed_erdos(10, .5)
g = rand_weights(d)
samples = g.sample(100)

os.makedirs("tests/data/bge_data/", exist_ok=True)
np.save("tests/data/bge_data/samples.npy", samples)
np.save("tests/data/bge_data/dag_amat.npy", d.to_amat()[0])

