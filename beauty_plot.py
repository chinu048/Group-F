import matplotlib.pyplot as plt
import numpy as np
def plotting(ans1,time1):
    plt.plot(ans1,time1)
    plt.show()

    
def main():
    plotting(np.arange(0,10,1),np.arange(0,1,0.1))

if __name__ == '__main__':
    main()
