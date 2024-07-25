import numpy as np
import matplotlib.pyplot as pp

x = np.linspace(0, 2 * np.pi, 360)
y = np.sin(x)

print(x)
print(y)

pp.plot(x, y)
# Add a "x-" after y to cross each value or "x" to cross them without a connecting line

pp.plot(x, np.cos(x))

pp.plot(x, y * np.cos(x))

pp.show()