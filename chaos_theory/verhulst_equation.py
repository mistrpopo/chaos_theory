import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

spaceresolution = 100
timeresolution = 60

fig, ax = plt.subplots()
x = np.linspace(0,1,spaceresolution)
line, = ax.plot(x, x*(1-x))

def draw(u):
    line.set_ydata(x*u*(1-x))
    return line,

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.plot(x,x)
ani = animation.FuncAnimation(fig, draw, np.linspace(1,4,timeresolution), interval=10)
plt.show()