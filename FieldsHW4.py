import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import random
from matplotlib.ticker import AutoMinorLocator

"""
this was done brute force. pls dont judge. it was 4 am 
when i finished this bc i had a lot of other things to do.
more important things.

i know this is bad. i know this could have been way more efficient.
i know for loops exist.

btw this is homework 4 for fields. NOT for ECE 3304.

"""

fig, plot = plt.subplots(2, 2)

y = []

x = np.arange(start=-1, stop=0, step=0.001)
y = np.sqrt(((1 + (2/3) * np.cos(4 * np.pi * x)) ** 2) + ((2/3) * np.sin(4 * np.pi * x)) ** 2)
z = np.sqrt(((1 - (2/3) * np.cos(4 * np.pi * x)) ** 2) + ((2/3) * np.sin(4 * np.pi * x)) ** 2)
plot[0, 0].plot(x, y, label="|V(z)|")
plot[0, 0].plot(x, z, '--', label="Z0|I(z)|")
plot[0, 0].yaxis.tick_right()
plot[0, 0].set_xticks(np.arange(start=-1, stop=0, step=0.25))
plot[0, 0].set_yticks(np.arange(start=0, stop=2.5, step=0.5))
plot[0, 0].yaxis.set_minor_locator(AutoMinorLocator(n=2))
plot[0, 0].grid()
plot[0, 0].legend(loc="upper left")
plot[0, 0].set_title("Rl = 5Z0")


x = np.arange(start=-1, stop=0, step=0.001)
y = np.sqrt(((1 + (1/3) * np.cos(4 * np.pi * x)) ** 2) + ((1/3) * np.sin(4 * np.pi * x)) ** 2)
z = np.sqrt(((1 - (1/3) * np.cos(4 * np.pi * x)) ** 2) + ((1/3) * np.sin(4 * np.pi * x)) ** 2)
plot[0, 1].plot(x, y, label="|V(z)|")
plot[0, 1].plot(x, z, '--', label="Z0|I(z)|")
plot[0, 1].yaxis.tick_right()
plot[0, 1].set_xticks(np.arange(start=-1, stop=0, step=0.25))
plot[0, 1].set_yticks(np.arange(start=0, stop=2.5, step=0.5))
plot[0, 1].yaxis.set_minor_locator(AutoMinorLocator(n=2))
plot[0, 1].grid()
plot[0, 1].legend(loc="upper left")
plot[0, 1].set_title("Rl = 2Z0")


x = np.arange(start=-1, stop=0, step=0.001)
y = np.sqrt(((1 + (-1/3) * np.cos(4 * np.pi * x)) ** 2) + ((-1/3) * np.sin(4 * np.pi * x)) ** 2)
z = np.sqrt(((1 - (-1/3) * np.cos(4 * np.pi * x)) ** 2) + ((-1/3) * np.sin(4 * np.pi * x)) ** 2)
plot[1, 0].plot(x, y, label="|V(z)|")
plot[1, 0].plot(x, z, '--', label="Z0|I(z)|")
plot[1, 0].yaxis.tick_right()
plot[1, 0].set_xticks(np.arange(start=-1, stop=0, step=0.25))
plot[1, 0].set_yticks(np.arange(start=0, stop=2.5, step=0.5))
plot[1, 0].yaxis.set_minor_locator(AutoMinorLocator(n=2))
plot[1, 0].grid()
plot[1, 0].legend(loc="upper left")
plot[1, 0].set_title("Rl = Z0/2")


x = np.arange(start=-1, stop=0, step=0.001)
y = np.sqrt(((1 + (-2/3) * np.cos(4 * np.pi * x)) ** 2) + ((-2/3) * np.sin(4 * np.pi * x)) ** 2)
z = np.sqrt(((1 - (-2/3) * np.cos(4 * np.pi * x)) ** 2) + ((-2/3) * np.sin(4 * np.pi * x)) ** 2)
plot[1, 1].plot(x, y, label="|V(z)|")
plot[1, 1].plot(x, z, '--', label="Z0|I(z)|")
plot[1, 1].yaxis.tick_right()
plot[1, 1].set_xticks(np.arange(start=-1, stop=0, step=0.25))
plot[1, 1].set_yticks(np.arange(start=0, stop=2.5, step=0.5))
plot[1, 1].yaxis.set_minor_locator(AutoMinorLocator(n=2))
plot[1, 1].grid()
plot[1, 1].legend(loc="upper left")
plot[1, 1].set_title("Rl = Z0/5")




plt.show()
