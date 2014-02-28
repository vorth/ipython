

import math

zero = (0,0,0)
one = (1,0,0)
rho = (0,1,0)
sigma = (0,0,1)
rho_inv = (1,1,-1)
sigma_inv = (0,-1,1)

def neg(h) :
    a, b, c = h
    return ( -a, -b, -c )

def plus(h1,h2) :
    a, b, c = h1
    d, e, f = h2
    return ( a+d, b+e, c+f )

def minus(h1,h2) :
    a, b, c = h1
    d, e, f = h2
    return ( a-d, b-e, c-f )

def times(h1,h2) :
    a, b, c = h1
    d, e, f = h2
    return ( a*d + b*e + c*f,
             a*e + b*d + b*f + c*e + c*f,
             a*f + b*e + b*f + c*d + c*e + c*f )

rho_sigma = times( rho, sigma )
rho_2 = times( rho, rho )
sigma_2 = times( sigma, sigma )

# some quick-and-dirty manual unit testing

# print( rho_sigma )  # should be (0, 1, 1)
# print( rho_2 )      # should be (1, 0, 1)
# print( sigma_2 )    # should be (1, 1, 1)
# print( times( sigma, sigma_inv ) )    # should be (1, 0, 0)
# print( times( (1,-1,-1), (0,-1,1) ) ) # should be (0, -2, 1)


sigma_value = 1 / (2* math.sin(math.pi/14))

rho_value = 2*math.sin(5*math.pi/14)

# This function maps from the heptagon field to the real numbers
# (as floating point values), so that we can render graphics.
def asReal(h):
    a, b, c = h
    return a + b*rho_value + c*sigma_value
