from math import pi

def format_angle(x):
    x = _round_real(x/pi)
    if x == 0:
        return '0'
    elif x == 1:
        return f'pi'    
    else:
        x = f'{x}pi'
    return x

def format_state(state):
    x1 = round_complex(state[0], 3)    
    x2 = round_complex(state[1], 3)
    return f'[{x1}, {x2}]'

def format_xyz(x, y, z):
    if int(x) == x:
        x = int(x)
    else:
        x = round(x, 3)
    if int(y) == y:
        y = int(y)
    else:
        y = round(y, 3)
    if int(z) == z:
        z = int(z)
    else:
        z = round(z, 3)
    return f'({x}, {y}, {z})'

def _round_real(x):
    return round(x, 10)

def round_complex(x, precision=10):
    return round(x.real, precision) + 1j*round(x.imag, precision)