import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


class DTSignalPlot:
    """
    coefficient: coefficient of the function
    frequency: w0 (in radians per sample)
    samples: samples n
    Description: Outputs a stem chart of the discrete-time signal
    """

    def __init__(self, coefficient, frequency, samples):
        self.coefficient = coefficient
        self.frequency = frequency
        self.samples = samples


    def getplot(self):
        """
        Creates a plot of the discrete-time signal
        """
        x = self.coefficient * np.cos(self.frequency * self.samples)
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title('Plot of DT signal: {} * cos({} * pi * n)'.format(self.coefficient, self.frequency))
        plt.stem(self.samples, x)
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

