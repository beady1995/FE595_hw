# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:35:48 2020

@author: Pengfei Liu
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi,100)
sinx=np.sin(x)
cosx=np.cos(x)

plt.plot(x,sinx,label='sin(x)')
plt.plot(x,cosx,label='cos(x)')
plt.legend()
plt.ylabel('y')
plt.xlabel('x')
plt.title('Sine wave and Cosine wave')
plt.show()