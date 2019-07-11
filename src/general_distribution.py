import matplotlib.pyplot as plt
import math


class Distribution:

    def __init__(self, mu=0, sigma=1):
        """
        Generic distribution class for calculating and
        visualizing a probability distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard dev of the distribution
            data (list of floats) a list of floats extracted from data file
        """
        self.mean = mu
        self.stdev = sigma
        self.data = []

    @staticmethod
    def n_choose_k(n, k):
        """
        Returns count of combinations

        Args:
            n (int): total number of trials
            k (int): chosen number of trials

        Returns:
        """
        f = math.factorial
        return f(n) / f(k) / f(n - k)

    def plot_histogram(self):
        """
        Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Returns:
            None
        """
        plt.figure()
        plt.hist(self.data)
        plt.xlabel('Data')
        plt.ylabel('Count')
        plt.title('Histogram of Data')

    def plot_bar_pdf(self, n_spaces=50):
        """
        Function to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """
        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(nrows=2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for '
                          '\n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def read_data_file(self, file_name):
        """
        Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are
        stored in the data attribute.

        Args:
            file_name (string): name of a file to read from

        Returns:
            None
        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
