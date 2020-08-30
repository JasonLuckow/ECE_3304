"""
Author: Jason Luckow
Date: 8/28/2020
Description: Outputs a stem chart of a list of discrete-time signals
"""

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import random


class DTSignalPlot:
    """
    coefficient: coefficient of the function
    frequency: w0 (in radians per sample)
    samples: samples n
    """
    def __init__(self, coefficient, frequency, samples):
        if len(coefficient) % 2 != 0 and len(frequency) % 2 != 0 and np.sqrt(len(frequency)) - int(np.sqrt(len(frequency))) != 0:
            # adds another signal to the list if the list has an odd number of signals
            coefficient.append(0)
            frequency.append(0)

        self.coefficient = coefficient
        self.frequency = frequency
        self.samples = samples
        self.signals = []

        for coefficients, frequencies in zip(self.coefficient, self.frequency):
            # zip takes the lists from the user and pairs data from each list
            # to  return an iterator
            self.signals.append(coefficients * np.cos(frequencies * self.samples))
            # initializes the list that will hold the signals

    def getstemplot(self):
        """
        Creates a figure of plots of the discrete-time signal based on
        how many signals are in the list
        """

        count = 0
        size = len(self.signals)
        factors = []
        pltloc1 = 0
        pltloc2 = 0

        for i in range(1, size + 1):
            if size % i == 0:
                factors.append(i)
                # finds the factor of the size of the signals list

        if np.sqrt(len(self.signals)) - int(np.sqrt(len(self.signals))) == 0:
            pltloc1 = np.sqrt(size)
            pltloc2 = np.sqrt(size)
            # takes care of perfect square condition
        elif len(factors) % 2 == 0:
            pltloc1 = factors[int(len(factors) / 2)]
            pltloc2 = factors[int(len(factors) / 2 - 1)]
            # since the list of factors is sorted and the length of the list is odd, grab the
            # two number that would make up the median and set them as 2D array indices for subplots

        fig, plot = plt.subplots(int(pltloc2), int(pltloc1))
        # creates subplots
        fig.suptitle('Stem Plot of Signals')
        for x in range(0, int(pltloc2)):
            for y in range(0, int(pltloc1)):
                label = '{} * cos({} * pi * n)'.format(self.coefficient[count], Fraction(self.frequency[count] / np.pi))
                # creates the label for the legend
                color = '#' + str(hex(random.randint(0, 16777215))[2:])
                # generates a random hex color code. Could be made into its own class
                plot[x, y].stem(self.samples, self.signals[count], color, label=label, basefmt=color)
                # basefmt is used here to configure the legend
                plot[x, y].grid()
                plot[x, y].legend(loc="upper right")
                plot[x, y].axhline(y=0, color='r')
                # adds horizontal line to the x axis on each subplot
                plot[x, y].set_xticks(range(self.samples[0], self.samples[-1] + 1, 2))
                # adds xticks to each subplot
                plot[x, y].set_xlabel('n')
                plot[x, y].set_ylabel('x[n]')
                count += 1
                # count is increased to correctly access lists of signals
        plt.show()

    def getperiod(self):
        """
        Converts the frequency w0 to fraction form, stripes pi from the input and returns the period N
        of the discrete-time signal in a list. Could also return constant k if added
        """
        periodN = []
        for freq in self.frequency:
            w0fraction = Fraction(freq / np.pi)
            periodN.append(w0fraction.denominator * 2)
        return periodN


# Python Project 1
sigset = DTSignalPlot([1, 1, 1, 1], [0, np.pi / 8, np.pi / 4, np.pi], np.arange(start=-15, stop=16))
sigset.getstemplot()
# generates plot
print(sigset.getperiod())
# generates list of the periods

