The Optical Bloch Equations give the time evolution of a two-state quantum system interacting with monochromatic electromagnetic radiation (in a system where there is some form of decay). The equations give the time evolution of a quantity called the Bloch Vector, which fully specifies the density matrix of the system. 

My code solves the Optical Bloch Equations for a given set of parameters, initial conditions and range of time values (using the solve_ivp function from the scripy.integrate library) and plots the results on an animated 3D Bloch Sphere (using the QuTiP library) 

Bloch.py contains the Bloch class, which contains functions for solving the Bloch Equations and plotting the results. Bloch_Equations.ipynb contains some discussion of the solutions, solved for different parameters. 
