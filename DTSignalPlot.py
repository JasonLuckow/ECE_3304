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
        self.signal = []
        for coefficients, frequencies in zip(self.coefficient, self.frequency):
            self.signal.append(coefficients * np.cos(frequencies * self.samples))

    def getplot(self):
        """
        Creates a plot of the discrete-time signal
        """
        colors = ['co', 'go', 'bo', 'ko']
        # 'o' adds dot to the tips of the plot
        # initializes the list that will hold the functions
        count = 0
        # for coefficients, frequencies in zip(self.coefficient, self.frequency):
        #     # zip takes the lists from the user and pairs data from each list
        #     # to  return an iterator
        #     label = '{} * cos({} * pi * n)'.format(coefficients, Fraction(frequencies/np.pi))
        #     # creates label for legend
        #     x.append(coefficients * np.cos(frequencies * self.samples))
        #     # stores unit sample signal to be plotted
        #     plt.stem(self.samples, x[count], colors[count], label=label, basefmt=" ", markerfmt=colors[count])
        #     # plots the stored unit sample signal. basefmt and markerfmt is used to configure legend
        #     count += 1
        for signals in self.signal:
            label = '{} * cos({} * pi * n)'.format(self.coefficient[count], Fraction(self.frequency[count] / np.pi))
            plt.stem(self.samples, signals, colors[count], label=label, basefmt=" ", markerfmt=colors[count])
            count += 1

        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title('Plot of DT signals')
        plt.axhline(y=0, color='r')
        # adds horizontal line to the x axis
        plt.legend()
        plt.xticks(self.samples)
        plt.grid()
        plt.show()


    def getperiod(self):
        """
        Converts the frequency w0 to fraction form and returns the period N
        of the discrete-time signal
        """
        w0fraction = Fraction(self.frequency)
        periodN = w0fraction.denominator * 2
        return periodN


#newplot = DTSignalPlot(4, 3/4 * np.pi, np.arange(start=-5, stop=6))
#newplot.getplot()
#newplot.getperiod()

newplot = DTSignalPlot([1, 1, 1, 1], [0, np.pi / 8, np.pi / 4, np.pi], np.arange(start=-10, stop=11))
newplot.getplot()

