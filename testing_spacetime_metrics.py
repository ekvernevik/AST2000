# Importing modules
import matplotlib.pyplot as plt
from math import pi
import mpl_toolkits.mplot3d.axes3d as axes3d
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Setting up coord.sys. and params
RMAX = 3
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
plt.style.use('dark_background')
fig.patch.set_facecolor('xkcd:black')
ax.set_facecolor('black') 
ax.grid(True) 
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

phi = np.linspace(0, 2*pi, 200)
r = np.linspace(-RMAX, RMAX, 200) #change -rmax to 0 for alcubierre
r, phi = np.meshgrid(r, phi, indexing='ij')

"""
Here only the Alcubierre Drive is being plotted. 
To plot the Wormhole or Black Hole, simply add/remove the '#'.
Enjoy! :)
"""

#Black Hole
#z = (r*2-1)**(1/2)
#rho = r

#Wormhole
#z = np.arcsinh(r)
#rho = np.cosh(z)

#Alcubierre Drive (change -RMAX to 0 for r =)
z = (1-(r-2)**2+((1-(r-2)**2)**2)**0.5)*np.cos(pi*r/2)*np.cos(phi)
rho = r

#Coordinate Transformation
X = rho*np.cos(phi)
Y = rho*np.sin(phi)
Z = z

# Surface
surf = ax.plot_surface(X, Y, Z, cmap=cm.plasma,#change plasma to change color mapping, look up matplotlib color
                       linewidth=0, antialiased=False)

# Color bar
fig.colorbar(surf, shrink=0.5, aspect=10)
    
# Animation (so pleased with how this turned out)
for angle in range(0, 80):
    ax.view_init(45-30*np.cos(angle/20), angle)
    plt.draw()
    plt.pause(0.01)

ax.set_xlim(-RMAX, RMAX)
ax.set_ylim(-RMAX, RMAX)
ax.set_zlim(-RMAX, RMAX)
