
zero = (0,0,0)
one = (1,0,0)
rho = (0,1,0)
sigma = (0,0,1)
rho_inv = (1,1,-1)
sigma_inv = (0,-1,1)

def neg( h ) :
    a, b, c = h  # this assigment syntax "unpacks" the tuple
    return ( -a, -b, -c )

def plus( h1, h2 ) :
    a, b, c = h1
    d, e, f = h2
    return ( a+d, b+e, c+f )

def minus( h1, h2 ) :
    a, b, c = h1
    d, e, f = h2
    return ( a-d, b-e, c-f )

def times( h1, h2 ) :
    a, b, c = h1
    d, e, f = h2
    return ( a*d + b*e + c*f,
             a*e + b*d + b*f + c*e + c*f,
             a*f + b*e + b*f + c*d + c*e + c*f )

rho_sigma = times( rho, sigma )
rho_2 = times( rho, rho )
sigma_2 = times( sigma, sigma )

