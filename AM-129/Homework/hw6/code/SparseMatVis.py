'''
A module to visualize the results of the Sparse Matrix
'''

__author__ = 'Simon Lee, siaulee@ucsc.edu'

import numpy as np
import matplotlib.pyplot as plt

def S(x):
    ps = 0.75*np.exp(-np.abs(x-0.25))
    return ps/np.sum(ps)

def Plot():
    #load in data
    data = np.loadtxt("./dist.dat")
    
    #parse the data to extract x components and y components
    x = data[:,0]
    y = data[:,1]
    line2 = S(x)

    #plot figure
    plt.figure(figsize=(12,8))
    plt.plot(x,y, 'k')
    plt.plot(x,line2, 'r--')
    plt.grid()
    plt.ylabel('Probability')
    plt.xlabel('X')
    plt.title("Stationary PMF of particle position (N=200, BIAS=0.001)");
    plt.legend((r'$P_{part}(x)$','$S(x)$'), loc='upper right')
    plt.savefig('SpareMat.png')
    plt.show()
    

if __name__=="__main__":
    Plot()
