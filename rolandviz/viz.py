from types import prepare_class
import numpy as np
import matplotlib.pyplot as plt

class PlotBasicFunction:

    def __init__(self):
        self.Ndim = 1000
        self.__X = self.__prepare_data()

    def plot_x2(self):
        fig = plt.figure(figsize=(6,5))
        plt.plot(self.__X, self.__X**2 ) 
        plt.savefig('x2.png')    
    
    def plot_sinx(self):
        fig = plt.figure(figsize=(6,5))
        plt.plot(self.__X, np.sin(self.__X))
        plt.savefig('sinx.png')

    def __prepare_data(self):
        return np.linspace(0., 10., self.Ndim, dtype='float')    
