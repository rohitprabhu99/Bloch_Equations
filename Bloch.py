import numpy as np
import qutip
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt, animation as anim
from mpl_toolkits.mplot3d import Axes3D

class Bloch:
    """
    A class that solves the optical Bloch equations (using Scipy Integrate) and
    plots the result (using the QuTiP library). The plot includes both the Bloch
    vector, R = (u, v, w), and the vector W = (omega, 0, delta)
    """
    def __init__(self, gamma, delta, omega, t_range, R0):
      self.gamma = gamma #Decay rate
      self.omega = omega #Rabi frequency
      self.delta = delta #Detuning (N.B. this needs to be a function of time)
      self.t_range = t_range #Range of time values
      self.R0 = R0 #Initial Bloch vector
    
      self.solve_Bloch()
    
    
    
    def solve_Bloch(self):
    
      def f (t, R):
        #Defining the optical Bloch equations, in the form dR/dt = f(t,R), where R = [u,v,w]
        dRdt = [(self.delta(t) * R[1] - (self.gamma/2)*R[0])/self.omega,
            (-self.delta(t) * R[0] + self.omega * R[2] - (self.gamma/2)*R[1])/self.omega,
            (-self.omega * R[1] - self.gamma*(R[2] - 1))/self.omega]
    
        return dRdt
    
      #Solving equations
      self.R = solve_ivp(fun = f, t_span = [self.t_range[0], self.t_range[-1]], t_eval = self.t_range, y0 = self.R0)
      
    
    def plot (self):
      #Animating the solution
      #Using code from: https://qutip.org/docs/latest/guide/guide-bloch.html
    
      fig = plt.figure()
      ax = Axes3D(fig, azim=-40, elev=30)
      sphere = qutip.Bloch(axes=ax)
    
      def animate(i):
        sphere.clear()
        sphere.add_vectors([[self.omega, 0, self.delta(self.R.t[i])],self.R.y[:, i]])
        sphere.make_sphere()
        return ax
    
      def init():
        return ax
    
    
    
      self.anim = anim.FuncAnimation(fig, animate, np.arange(np.shape(self.R.y)[1]),
                                    init_func=init, blit=False, repeat=False);
      
      
    
    
      plt.close()
