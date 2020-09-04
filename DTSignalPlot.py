"""
Author: Jason Luckow
Date: 9/2/2020
Description: Outputs a stem chart of a list of discrete-time signals
"""

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import random
from matplotlib.ticker import AutoMinorLocator


class DTSignalPlot:
    """
    Optional args:
        samples: samples n as a range of numbers
    """
    def __init__(self, **kwargs):
        samples = kwargs.get('samples', None)
        self.samples = samples
        self.coefficients = []
        self.frequencies = []
        self.constantsK = []
        self.signals = []
        self.labels = []


    def getstemplot(self):
        """
        Creates a figure of plots of the discrete-time signals based on
        how many signals are in the list
        """
        oddgrid = False
        if len(self.signals) % 2 != 0 and np.sqrt(len(self.signals)) - int(np.sqrt(len(self.signals))) != 0:
            # adds another signal to the list if the list has an odd number of signals
            self.signals.append(0 * self.samples)
            self.coefficients.append(0)
            self.frequencies.append(0)
            oddgrid = True

        count = 0
        kcount = 0
        freqcount = 0
        flag = False
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
        # adds title to figure
        for x in range(0, int(pltloc2)):
            for y in range(0, int(pltloc1)):
                # iterates through all subplots to fill with signals
                color = "#{:06X}".format(random.randint(0, 0xFFFFFF))
                # generates a random hex color code. Could be made into its own class
                if isinstance(self.signals[count], list):
                    # runs this if signal is a unit sample sequence
                    label = ''
                    for z in range(0, len(self.coefficients[count]), 1):
                        # generates a title/label
                        if self.coefficients[count][z] != 0:
                            if flag is False:
                                if self.coefficients[count][z] > 0 and self.constantsK[kcount][z] >= 0:
                                    label += str(self.coefficients[count][z]) + '\u03B4[n+' + str(self.constantsK[kcount][z]) + ']'
                                elif self.coefficients[count][z] < 0 and self.constantsK[kcount][z] <= 0:
                                    label += str(self.coefficients[count][z]) + '\u03B4[n-' + str(-self.constantsK[kcount][z]) + ']'
                                elif self.coefficients[count][z] > 0 and self.constantsK[kcount][z] <= 0:
                                    label += str(self.coefficients[count][z]) + '\u03B4[n-' + str(-self.constantsK[kcount][z]) + ']'
                                elif self.coefficients[count][z] < 0 and self.constantsK[kcount][z] >= 0:
                                    label += str(self.coefficients[count][z]) + '\u03B4[n-' + str(-self.constantsK[kcount][z]) + ']'
                                flag = True

                            elif flag is True:
                                if self.coefficients[count][z] > 0 and self.constantsK[kcount][z] >= 0:
                                    label += '+' + str(self.coefficients[count][z]) + '\u03B4[n+' + str(self.constantsK[kcount][z]) + ']'
                                elif self.coefficients[count][z] < 0 and self.constantsK[kcount][z] <= 0:
                                    label += '-' + str(-self.coefficients[count][z]) + '\u03B4[n-' + str(-self.constantsK[kcount][z]) + ']'
                                elif self.coefficients[count][z] > 0 and self.constantsK[kcount][z] <= 0:
                                    label += '+' + str(self.coefficients[count][z]) + '\u03B4[n-' + str(-self.constantsK[kcount][z]) + ']'
                                elif self.coefficients[count][z] < 0 and self.constantsK[kcount][z] >= 0:
                                    label += '-' + str(-self.coefficients[count][z]) + '\u03B4[n-' + str(self.constantsK[kcount][z]) + ']'

                    if pltloc1 == 2 and pltloc2 == 1:
                        plot[y].stem(self.signals[count][1], self.signals[count][0], color)
                        # grabs the correct signal with count then plots constantsK [1] for x samples
                        # and coefficients [0] for height of stem
                        plot[y].set_xticks(range(min(self.signals[count][1]) - 2, max(self.signals[count][1]) + 3, 2))
                        # adds xticks to each subplot
                        plot[y].xaxis.set_minor_locator(AutoMinorLocator(n=2))
                        # adds ticks in between numbered ticks from above
                    else:
                        plot[x, y].stem(self.signals[count][1], self.signals[count][0], color)
                        # grabs the correct signal with count then plots constantsK [1] for x samples
                        # and coefficients [0] for height of stem
                        plot[x, y].set_xticks(range(min(self.signals[count][1]) - 2, max(self.signals[count][1]) + 3, 2))
                        # adds xticks to each subplot
                        plot[x, y].xaxis.set_minor_locator(AutoMinorLocator(n=2))
                        # adds ticks in between numbered ticks from above
                    flag = False
                    kcount += 1
                else:
                    # runs this if signal is a complex sequence
                    label = '{} * cos({} * \u03C0 * n)'.format(self.coefficients[count], self.frequencies[freqcount])
                    if pltloc1 == 2 and pltloc2 == 1:
                        plot[y].stem(self.samples, self.signals[count], color, basefmt=color)
                        plot[y].set_xticks(range(self.samples[0], self.samples[-1] + 1, 2))
                        # adds xticks to each subplot
                        plot[y].xaxis.set_minor_locator(AutoMinorLocator(n=2))
                        # adds ticks in between numbered ticks from above
                    else:
                        plot[x, y].stem(self.samples, self.signals[count], color, basefmt=color)
                        # basefmt is used here to configure the legend
                        plot[x, y].set_xticks(range(self.samples[0], self.samples[-1] + 1, 2))
                        # adds xticks to each subplot
                        plot[x, y].xaxis.set_minor_locator(AutoMinorLocator(n=2))
                        # adds ticks in between numbered ticks from above
                    freqcount += 1

                if pltloc1 == 2 and pltloc2 == 1:
                    plot[y].set_title(label)
                    # adds title to each subplot
                    plot[y].grid()
                    plot[y].legend(loc="upper right")
                    plot[y].axhline(y=0, color='r')
                    # adds horizontal line to the x axis on each subplot
                    plot[y].set_xlabel('n')
                    plot[y].set_ylabel(self.labels[count])
                else:
                    plot[x, y].set_title(label)
                    # adds title to each subplot
                    plot[x, y].grid()
                    plot[x, y].legend(loc="upper right")
                    plot[x, y].axhline(y=0, color='r')
                    # adds horizontal line to the x axis on each subplot
                    plot[x, y].set_xlabel('n')
                    plot[x, y].set_ylabel(self.labels[count])
                count += 1
                # count is increased to correctly access lists of signals
        if oddgrid is True:
            fig.delaxes(plot[-1, -1])
        #plt.tight_layout()
        plt.show()

    def getconvolution(self, xn, hn):
        """
        Takes two signals as lists, computes the convolution of the two, then
        returns the data of the convoluted signal as two separate lists
        """
        yn = {}
        # creates a dictionary to store the convoluted signal
        hcount = 0
        xcount = 0
        for coefficienth in hn[1]:
            # iterates through each index in the second signal, the signal being convoluted,
            # to make sure it is "shifted"
            for coefficientx in xn[1]:
                # iterates through each index in the first signal to "shift" the signal being convoluted
                index = coefficienth + coefficientx
                # index created to make the key of the dictionary
                if index not in yn:
                    yn[index] = []
                    # initializes a list for index if the index is not yet in the dictionary
                yn[index].append(hn[0][hcount] * xn[0][xcount])
                # value is added to the list at the dictionaries index
                # to keep track of the different coefficients at different signal shifts
                xcount += 1

            xcount = 0
            hcount += 1

        #print(yn.items())
        # uncomment the above line to see the dictionary created.
        # the keys represent the what index the shift happened at
        # the values show all coefficients that occurred at that index as a list

        constants = []
        coefficients = []
        for constantK, coefficient in yn.items():
            constants.append(-constantK)
            coefficients.append(sum(coefficient))
            # since the coefficients of each shift are stored as a list, all values inside
            # the list at each index are summed then appended to another list to
            # hold convoluted coefficient values

        return coefficients, constants

    def addcomplexplot(self, coefficient, frequency, constantPhi):
        """
        adds a complex sequence, such as a cos(), to the signals variable
        """
        self.signals.append(coefficient * np.cos(frequency * self.samples + constantPhi))
        self.frequencies.append(Fraction(frequency / np.pi))
        self.coefficients.append(coefficient)

    def addunitsampleplot(self, coefficients, constantsK, label):
        """
        adds a unit sample sequence to the signals variable
        returns the data entered as a single list
        """
        self.constantsK.append(constantsK)
        self.coefficients.append(coefficients)
        self.signals.append([coefficients, [-x for x in constantsK]])
        self.labels.append(label)

        return [coefficients, [-x for x in constantsK]]
        # goes through each value in constantsK and makes them negative

    def getperiod(self):
        """
        Converts the frequency w0 to fraction form, stripes pi from the input and returns the period N
        of the discrete-time signal in a list. Could also return constant k if added
        """
        periodN = []
        for freq in self.frequencies:
            w0fraction = Fraction(freq / np.pi)
            periodN.append(w0fraction.denominator * 2)

        return periodN


# # ECE 3304 Python Project 1
# sigset = DTSignalPlot(samples=np.arange(start=-15, stop=16))
# sigset.addcomplexplot(1, 0, 0)
# sigset.addcomplexplot(1, np.pi / 8, 0)
# sigset.addcomplexplot(1, np.pi / 4, 0)
# sigset.addcomplexplot(1, np.pi, 0)
# print(sigset.getperiod())
# sigset.getstemplot()

# ECE 3304 Python Project 2

""" Test Case 1 """
sigset1 = DTSignalPlot(samples=np.arange(start=-15, stop=16))
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
# adds the convoluted signal to the plot

""" Test Case 2 """
# the samples argument is optional but necessary if adding complex plot

n = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
seq3 = [0, 0, 0, 3, 0, 4, 0, 0, -2, 0, 0]
seq4 = [0, 0, 0, 0, 0, 3, 2, 1,  0, 0, 0]

x2 = sigset1.addunitsampleplot(seq3, n, "x1[n]")
h2 = sigset1.addunitsampleplot(seq4, n, "h1[n]")
# two unit sample sequences that will be convoluted

convcoef1, convconst1,  = sigset1.getconvolution(x2, h2)
# returns lists that are needed for adding a new unit sample plot
sigset1.addunitsampleplot(convcoef1, convconst1, "y1[n] (Convoluted Plot)")
# adds the convoluted signal to the plot
sigset1.getstemplot()
# generates plot