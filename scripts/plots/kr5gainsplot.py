# -*- coding: utf-8 -*-

#
# Plots for kr5
#

from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt

folder = '../../../data/kr5/'

# Read the files
x_5 = np.loadtxt(folder+"kr5_k.5_f2_Hand.txt")
x1 = np.loadtxt(folder+"kr5_k1_f2_Hand.txt")
x2 = np.loadtxt(folder+"kr5_k2_f2_Hand.txt")
x5 = np.loadtxt(folder+"kr5_k5_f2_Hand.txt")
x10 = np.loadtxt(folder+"kr5_k10_f2_Hand.txt")
# Desired trajectory
xd = np.loadtxt(folder+"kr5_k1_f2_Hand_des.txt")

plt.plot(xd[:,0], xd[:,2], 'k--')
plt.plot( x_5[:1400,0], x_5[:1400,2])
plt.plot( x1[:,0], x1[:,2])
plt.plot( x2[:,0], x2[:,2])
plt.plot( x5[:1400,0], x5[:1400,2])
plt.plot(x10[:,0], x10[:,2])
# plt.legend((r'$y_d$',r'$y$ con $\lambda=0.5$',r'$y$ con $\lambda=1$',
#             r'$y$ con $\lambda=2$',r'$y$ con $\lambda=5$',
#             r'$y$ con $\lambda=10$'))
plt.legend((r'$y_d$',r'$\lambda=0.5$', r'$\lambda=1$', r'$\lambda=2$',
            r'$\lambda=5$', r'$\lambda=10$'))
plt.xlabel('tiempo [s]')
plt.ylabel('eje y [m]')
plt.title('Trayectoria para diferentes ganancias')
plt.grid()
plt.show()
