import DTSignalPlot as dt
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import random
from matplotlib.ticker import AutoMinorLocator

"""
This file is really only used to test oop concepts for other applications.
It constantly changes and it is really only for my testing purposes.
"""

for i in range(5):
    print(i)

sigset1 = dt.DTSignalPlot(samples=np.arange(start=-15, stop=16))
# the samples argument is optional but necessary if adding complex plot

xn = [3, 2, 1, -1, -2, -3]
hn = [0, -1, -2]
seq1 = [3, 2, 1, -1, -2, -3]
seq2 = [1, 1, 1]

x1 = sigset1.addunitsampleplot(seq1, xn, "x0[n]")
h1 = sigset1.addunitsampleplot(seq2, hn, "h0[n]")
# two unit sample sequences that will be convoluted

convcoef0, convconst0,  = sigset1.getconvolution(x1, h1)
# returns lists that are needed for adding a new unit sample plot
sigset1.addunitsampleplot(convcoef0, convconst0, "y0[n] (Convoluted Plot)")

sigset1.getplot()