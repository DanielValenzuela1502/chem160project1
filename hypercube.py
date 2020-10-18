import numpy as np
from random import choice
import math
dim=30
trials=1000
for i in range(dim):
    for j in range(trials):
        point1=np.random.random()
        point2=np.random.random()
        distance=abs(point1-point2)
        if distance > 0:
            store=np.array(distance)
            break
    mean=np.mean(store)
    print(mean)