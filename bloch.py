import numpy as np
from cmath import phase
from math import cos, sin, acos, e
from utils import normalize_vector

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
    return np.array([x, y, z])

def rotation_trace_points(n, A, B, alpha, total_points=50):
    # Создаем ортонормированные базисные векторы i и j в плоскости вращения.
    # при этом i указывает на дугу вращения и делит ее пополам.
    R = np.linalg.norm((B - A)) / (2*sin(abs(alpha)/2))
    j = normalize_vector(np.array(B) - np.array(A))
    if alpha > 0:
        i = np.cross(j, n)
        r0 = B - R*(cos(alpha/2)*i + sin(alpha/2)*j)
    else:
        i = np.cross(n, j)
        r0 = A - R*(cos(alpha/2)*i + sin(alpha/2)*j)

    circle_point = lambda i, j, r0, R, phi: r0 + R*cos(phi)*i + R*sin(phi)*j
    angles = np.linspace(-alpha/2, alpha/2, total_points)
    points = [circle_point(i, j, r0, R, phi) for phi in angles]

    return points