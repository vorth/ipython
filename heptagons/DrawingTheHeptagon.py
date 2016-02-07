
# load the definitions from the previous notebook
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


# represent points or vertices as pairs of heptagon numbers

p0 = ( zero, zero )
p1 = ( sigma, zero )
p2 = ( plus( one, sigma ), rho )
p3 = ( sigma, rho_sigma )
p4 = ( zero, sigma_2 )
p5 = ( neg( rho ), rho_sigma )
p6 = ( neg( rho ), rho )

heptagon = [ p0, p1, p2, p3, p4, p5, p6 ]

heptagram_rho = [ p0, p2, p4, p6, p1, p3, p5 ]

heptagram_sigma = [ p0, p3, p6, p2, p5, p1, p4 ]


import math

sigma_real = 1 / (2* math.sin(math.pi/14))

rho_real = 2*math.sin(5*math.pi/14)

# This function maps from the heptagon field to the real numbers
# (as floating point values), so that we can render graphics.
def asReal(h):
    a, b, c = h
    return a + b*rho_real + c*sigma_real

# This function maps from a pair of heptagon numbers to
#  a pair of floating point numbers (approximating real numbers)
def render( v ):
    x, y = v
    return [ asReal(x), asReal(y) ]


import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
Path = mpath.Path

def drawPolygon( polygonVerts, color, mapping=render ):
    n = len( polygonVerts )
    codes = [ Path.MOVETO ]
    verts = []
    verts .append( mapping( polygonVerts[ 0 ] ) )
    for i in range(1,n+1):
        codes.append ( Path.LINETO )
        verts.append ( mapping( polygonVerts[ i % n ] ) )
    path = mpath.Path( verts, codes )
    return mpatches.PathPatch( path, facecolor='none', edgecolor=color )

def drawHeptagrams( mapping=render ):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.add_patch( drawPolygon( heptagon,'#dd0000', mapping ) )
    ax.add_patch( drawPolygon( heptagram_rho,'#990099', mapping ) )
    ax.add_patch( drawPolygon( heptagram_sigma,'#0000dd', mapping ) )
    ax.set_xlim(-3,4)
    ax.set_ylim(-1,6)

def skewRender(v):
    x = asReal( v[0] )
    y = asReal( v[1] )
    x = x + y/(2*sigma_real)
    y = math.sin( (3.0/7.0) * math.pi ) * y
    return [ x, y ]

