## Introduction
The Optical Bloch Equations give the time evolution of a two-state quantum system interacting with monochromatic electromagnetic radiation (in a system where there is some form of decay). The equations give the time evolution of a quantity called the Bloch Vector, which fully specifies the density matrix of the system. 


## Implementation
The solution is implemented in a single class (*Bloch*). An object of this class is initialised with the physical parameters of the system (the decay rate, the Rabi frequency, the detunbing, the initial Bloch vector, and the range of times of interest). The class contains two functions, one to solve the Optical Bloch Equations (using the solve_ivp function from the scripy.integrate library) and one to plot the results on an animated 3D Bloch Sphere (using the QuTiP library) 

## Files
*Bloch.py* contains the *Bloch* class, which contains functions for solving the Bloch Equations and plotting the results on an animated graph. *Bloch_Equations.ipynb* contains some discussion of the solutions, solved for different parameters. 

## How to use
To use the *Bloch* class, run the following code (with parameter values filled in):

```
from Bloch import Bloch

system = Bloch(gamma = , delta = , omega = , t_range = , R0 = )
system.plot()


```
where ```gamma``` is a float, ```delta``` is a function (of time), ``` omega``` is a float, ```t_range``` is an array and ```R0``` is an list of floats (of length of 3)


