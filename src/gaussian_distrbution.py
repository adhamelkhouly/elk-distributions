import math
from .general_distribution import Distribution


class Gaussian(Distribution):
    """
    Gaussian distribution class for calculating and visualizing a
    Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data (list of floats) a list of floats extracted from the data file
    """

    def __init__(self, mu=0, sigma=1):
        super().__init__(mu, sigma)

    def __add__(self, other):
        """
        Function to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution
        """

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)

        return result

    def __repr__(self):
        """
        Function to output the characteristics of the Gaussian instance

        Returns:
            string: characteristics of the Gaussian
        """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

    def calculate_mean(self):
        """
        Function to calculate the mean of the data set.

        Returns:
            float: mean of the data set
        """

        avg = 1.0 * sum(self.data) / len(self.data)

        self.mean = avg

        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Function to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation of the data set
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean

        sigma = 0

        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma / n)

        self.stdev = sigma

        return self.stdev

    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(
            -0.5 * ((x - self.mean) / self.stdev) ** 2)

    def read_data_file(self, file_name, sample=True):
        """
        Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in data attribute.
        After reading in the file, the mean and standard dev are calculated

        Args:
            file_name (string): name of a file to read from
            sample (bool): boolean for sample vs population

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
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
