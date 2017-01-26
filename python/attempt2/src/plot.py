#---------------------------------------
# IMPORTS
#---------------------------------------

import findata

from matplotlib.finance import candlestick_ohlc

import matplotlib
import matplotlib.pyplot as plt

#---------------------------------------
# CLASSES
#---------------------------------------

class Plot(object):
    def __init__(self, ds):
        self.ds = ds
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)

        self.ax.xaxis_date()

        #plt.ion()

    def clear(self):
        self.ax.cla()

    def draw_line(self, x1, y1, x2, y2, color):
        self.ax.plot((x1, x2), (y1, y2), color=color)

    def pause(self, t=0.0):
        plt.pause(t)

    def set_legend(self, legend):
        legend = [matplotlib.patches.Patch(color=x[0], label=x[1]) for x in legend]

        plt.legend(handles=legend, loc="lower left")

    def plot_ref(self):
        quotes = self.ds.transform(findata.TIME,
                                   findata.OPEN_ASK,
                                   findata.HIGH_ASK,
                                   findata.LOW_ASK,
                                   findata.CLOSE_ASK)

        candlestick_ohlc(self.ax, quotes, width=0.001, colorup='#e0ffe0', colordown='#ffe0e0')

    def show(self):
        plt.show()
