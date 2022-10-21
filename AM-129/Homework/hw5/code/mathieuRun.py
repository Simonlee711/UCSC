'''
Python module to play around with os library in python
'''
__author__ = 'Simon Lee: siaulee@ucsc.edu'


import os
import numpy as np
import matplotlib.pyplot as plt

path = '/Users/simonlee/leesimon-am129-fall21/Homework/hw5/code'

def rebuild():
    os.chdir(path + "/MathieuFunctions")
    os.system('make clean mathieu.ex')
    os.chdir(path)

def build():
    os.chdir(path + "/MathieuFunctions")
    os.system('make')
    os.chdir(path)

def generate_input(N,q):
    
    exists = os.path.exists(path + "/MathieuFunctions/mathieu.init")
    backup = (path + "/MathieuFunctions/mathieu.init")
    if exists:
        os.chdir(path + "/MathieuFunctions")
        os.rename('mathieu.init','mathieu.init.bak')
        os.chdir(path) 
    # write into a file
    init_file = open(backup,"w+")
    # write 3 lines into init file
    
    init_file.write('numpoints '+ str(N) + '\n')
    init_file.write('q_index ' + str(q) + '\n')
    init_file.write('run_name Mathieu_'+ str(N) + '_' + str(q))
    init_file.close()
    


def run_mathieu(N,q):
    build()
    generate_input(N,q)
    os.chdir(path + "/MathieuFunctions")
    os.system('./mathieu.ex')
    os.chdir(path)

def parsweep_mathieu(N):
    # Range of q values to test
    qRange = np.arange(0,42,2)
    for q in qRange:
        run_mathieu(N,q)

def plot_parsweep(N,nPlot):
    # Set range and space to store data
    qRange = np.arange(0,42,2)
    evals = np.zeros([len(qRange),nPlot])
    # Open files and extract relevant data
    for idx,q in enumerate(qRange):
        fname = 'MathieuFunctions/data/Mathieu_' + str(N) + '_' + str(q) + '.dat'
        data = np.loadtxt(fname)
        evals[idx,:] = np.sort(data[:,1])[0:nPlot]
    
    #plot two equations
    equation1 = np.zeros(42)
    equation2 = np.zeros(42)
    for i in range(0, 42):
        equation1[i] = 1 + i - ((1/8)* pow(i,2)) - ((1/64)*pow(i,3))
        equation2[i] = 4 - ((1/12)*pow(i,2)) + ((5/13824) * pow(i,4)) 

    # Generate a plot of the eigenvalues as a function of the parameter q
    plt.figure(figsize=(12,8))
    plt.plot(qRange,evals,'-k')
    plt.plot(equation1,'b--')
    plt.plot(equation2,'b--')
    plt.ylim([-100, 100])
    plt.grid()
    plt.ylabel('Eigenvalues')
    plt.xlabel('Parameters')
    plt.title("Mathieu Functions Eigenvalue plot");
    plt.savefig('mathieu.png')
    plt.show()

if __name__=="__main__":
    N = 101
    rebuild()
    parsweep_mathieu(N)
    plot_parsweep(N,7)