# -*- coding: utf-8 -*-

#
# Plots for kr5
#

from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt


folder = '../../../data/kr5/'

flag=3
prefix = 'kr5_f' + str(flag) + '_'


# Read the files
path = folder + prefix
q = np.loadtxt(path+'q.txt')
x     = np.loadtxt(path+"Hand.txt")
xdes  = np.loadtxt(path+"Hand_des.txt")
stime = np.loadtxt(path+"time.txt")

# Set the plotting times
if (flag==1):
    tf = 900
    q = q[:tf,:]; x = x[:tf,:]; xdes = xdes[:tf,:]; stime = stime[:tf]
elif (flag==2):
    tf = 1000
    q = q[:tf,:]; x = x[:tf,:]; xdes = xdes[:tf,:]; stime = stime[:tf]
elif (flag==3):
    # tf = 1000
    # q = q[:tf,:]; x = x[:tf,:]; xdes = xdes[:tf,:]; stime = stime[:tf]
    pass

# Plot the temporal joint configuration
plt.plot(q[:,0], q[:,1:])
plt.xlabel('tiempo [s]')
plt.ylabel('Valor articular [rad]')
plt.title('Evolución articular en el tiempo')
plt.legend((r'$q_1$', r'$q_2$', r'$q_3$', r'$q_4$', r'$q_5$', r'$q_6$'), loc='best')
plt.grid()
plt.show()

# Plot position
#plt.plot(x[:,0], x[:,1:4])
plt.subplot(121)
plt.plot(x[:,0], x[:,1], linewidth=2)
plt.plot(x[:,0], x[:,2], linewidth=2)
plt.plot(x[:,0], x[:,3], linewidth=2)
plt.plot(xdes[:,0], xdes[:,1:4],'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición del efector final")
plt.legend(('x', 'y', 'z'), loc='best')
#plt.grid()
#plt.show()
# Plot orientation
plt.subplot(122)
plt.plot(x[:,0], x[:,4], linewidth=2)
plt.plot(x[:,0], x[:,5], linewidth=2)
plt.plot(x[:,0], x[:,6], linewidth=2)
plt.plot(x[:,0], x[:,7], linewidth=2)
plt.plot(xdes[:,0], xdes[:,4:], 'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('cuaternión')
plt.title('Orientación del efector final')
plt.legend((r'$\varepsilon_w$', r'$\varepsilon_x$', r'$\varepsilon_y$',
            r'$\varepsilon_z$'), loc="best")
#plt.axis('equal')
#plt.grid()
plt.show()

# Plot 3D
from mpl_toolkits.mplot3d import Axes3D
if (flag==1):
    ax = plt.figure().gca(projection='3d')
    ax.plot(x[:,1], x[:,2], x[:,3])
    ax.plot(xdes[1:2,1], xdes[1:2,2], xdes[1:2,3], 'ro')
    ax.set_xlabel(r'x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    ax.text(x[0,1], x[0,2], x[0,3],'inicial')
    ax.text(xdes[0,1], xdes[0,2], xdes[0,3],'final')
    ax.set_title('Trayectoria Cartesiana del efector final')
    plt.show()
elif (flag==2):
    #ax = plt.axes(projection='3d')
    ax = plt.figure().gca(projection='3d')
    ax.plot(x[:,1], x[:,2], x[:,3])
    ax.plot(xdes[:,1], xdes[:,2], xdes[:,3], 'r')
    ax.set_xlabel(r'x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    ax.set_xlim3d([0.5, 1.4])
    ax.set_zlim3d([0.2, 0.8])
    # plt.gca().set_aspect('equal', adjustable='box')
    # ax.set_aspect('equal'); plt.axis('scaled'); plt.axis('equal')
    plt.show()

elif (flag==3):
    ax = plt.figure().gca(projection='3d')
    ax.plot(xdes[:,1], xdes[:,2], xdes[:,3], 'r--')
    ax.plot(x[:,1], x[:,2], x[:,3])
    ax.set_xlabel(r'x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    ax.set_xlim3d([0.7, 1.3])
    ax.set_ylim3d([-0.1, 0.5])
    ax.set_zlim3d([0.3, 0.9])
    # plt.gca().set_aspect('equal', adjustable='box')
    # ax.set_aspect('equal'); plt.axis('scaled'); plt.axis('equal')
    plt.show()

# Plot computation time
plt.plot(stime)
plt.xlabel('iteración')
plt.ylabel('tiempo [ms]')
plt.title('Tiempo de cálculo')
plt.grid()
plt.show()
