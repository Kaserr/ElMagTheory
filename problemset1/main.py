import numpy as np
import scipy as sp
import matplotlib as plt
from sympy import *
from scipy.integrate import simps
import numba as nb
from numba import jit, njit, vectorize, float32, float64, int32
from time import time, time_ns
from NumbaQuadpack import quadpack_sig, dqags

# timer decorator
def timer(myFunc):
    def wrapper(*args, **kwargs):
        startTime = time_ns()
        myFunc(*args, **kwargs)
        runTime = time_ns()-startTime #strftime("%H:%M:%S", localtime(time()-startTime))
        print("Time taken: {} ns".format(runTime))
    return wrapper



@timer
def main():

    return

if __name__ == "__main__":
    main()