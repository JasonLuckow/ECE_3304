"""
Author: Jason Luckow
Date: 8/28/2020
"""

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


class DTSignalPlot:
    """
    coefficient: coefficient of the function
    frequency: w0 (in radians per sample)
    samples: samples n
    Description: Outputs a stem chart of a list of discrete-time signals
    """

    def __init__(self, coefficient, frequency, samples):
        self.coefficient = coefficient
        self.frequency = frequency
        self.samples = samples
        self.signals = []
        for coefficients, frequencies in zip(self.coefficient, self.frequency):
            # zip takes the lists from the user and pairs data from each list
            # to  return an iterator
            self.signals.append(coefficients * np.cos(frequencies * self.samples))
            # initializes the list that will hold the signals

    def getplot(self):
        """
        Creates a plot of the discrete-time signal
        """
        colors = ['co', 'go', 'bo', 'ko']
        # 'o' adds dot to the tips of the plot
        # initializes the list that will hold the functions
        count = 0
        fig, plot = plt.subplots(len(self.signals))
        fig.suptitle('Plotted Signals')
        for signal in self.signals:
            label = '{} * cos({} * pi * n)'.format(self.coefficient[count], Fraction(self.frequency[count] / np.pi))
            plot[count].stem(self.samples, signal, colors[count], label=label, basefmt=" ", markerfmt=colors[count])
            plot[count].grid()
            plot[count].legend(loc="upper right")
            plot[count].axhline(y=0, color='r')
            # adds horizontal line to the x axis
            plot[count].set_xticks(self.samples)
            plot[count].set_xlabel('n')
            plot[count].set_ylabel('x[n]')
            count += 1
        plt.show()


    def getperiod(self):
        """
        Converts the frequency w0 to fraction form, stripes pi from the input and returns the period N
        of the discrete-time signal in a list
        """
        periodN = []
        for freq in self.frequency:
            w0fraction = Fraction(freq / np.pi)
            periodN.append(w0fraction.denominator * 2)
        return periodN


newplot = DTSignalPlot([1, 1, 1, 1], [0, np.pi / 8, np.pi / 4, np.pi], np.arange(start=-15, stop=16))
newplot.getplot()
print(newplot.getperiod())

