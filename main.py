import random

import matplotlib.pyplot as plt

x = [0, 1, 0.5, 0]
y = [0, 0, 0.866, 0]

random_index = random.randint(0, 2)
Vx = x[random_index]
Vy = y[random_index]

u, v = sorted([random.random(), random.random()])
Px = x[0] * (1 - u - v) + x[1] * u + x[2] * v
Py = y[0] * (1 - u - v) + y[1] * u + y[2] * v

plt.plot(x + [x[0]], y + [y[0]], 'b-')
for _ in range(5000):
    random_index = random.randint(0, 2)
    Vx = x[random_index]
    Vy = y[random_index]
    Px = (Vx+Px) / 2
    Py = (Vy+Py) / 2
    plt.plot(Px, Py, 'ro')

plt.axis('equal')

plt.grid(False)
plt.show()
