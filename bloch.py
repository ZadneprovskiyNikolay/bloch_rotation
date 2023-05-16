import numpy as np
from cmath import phase
from math import cos, sin, acos, e

def state_to_bloch(state):    
    theta = 2*acos(abs(state[0]))
    phi = phase(state[1]) - phase(state[0])
    return theta, phi

def bloch_to_state(theta, phi):
    state = np.array([0j, 0j])
    state[0] = cos(theta/2)
    state[1] = sin(theta/2) * e**(1j*phi)
    return state

def xyz_from_bloch(theta, phi):
    x = cos(phi) * sin(theta)
    y = sin(phi) * sin(theta)
    z = cos(theta)
    return x, y, z
