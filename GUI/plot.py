import numpy as np
import matplotlib.pyplot as plt
import math


def beauty_plot(values_x,values_y,label_x = 'lols',label_y='lols',background_color= '#000000',line_color ='#AF0000',grid = True):
    # values = np.arange(0,10,1)
    ax = plt.subplot(111, facecolor = str(background_color))
    plt.xlabel(label_x,fontsize=14, color='red')
    plt.ylabel(label_y,fontsize=14, color='red')
    plt.title(label_y + ' Readings',fontsize = 18)
    plt.plot(values_x,values_y,str(line_color))
    plt.autoscale(tight =True)
    if grid is True:
        plt.grid()
    plt.show()
