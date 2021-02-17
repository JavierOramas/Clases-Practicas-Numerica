import numpy as np
import matplotlib.pyplot as plt
import math

plt.axes(projection = 'polar')

rads = np.arange(0,2*np.pi, 0.001)
a = 1.5

def generate_heart(size):
    for rad in rads:
        r = (math.sin(rad)*math.sqrt(abs(math.cos(rad))))/(math.sin(rad)+7/5)-2*math.sin(rad)+size
        plt.polar(rad,r,'r.')
        

i = 0
while i < 3:
    generate_heart(i)
    i+= 0.5
    
plt.savefig('javier_alejandro_oramas_lopez.png')