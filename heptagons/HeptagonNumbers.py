
# coding: utf-8


import math

class HeptagonNumber(object):

    def __init__( self, ones=0, rhos=0, sigmas=0 ):
        self.ones = ones
        self.rhos = rhos
        self.sigmas = sigmas

    def __add__( self, rhs ):  #self and rhs are HeptagonNumber objects
        a,b,c = self.ones, self.rhos, self.sigmas
        if isinstance( rhs, self.__class__ ):
            d,e,f = rhs.ones, rhs.rhos, rhs.sigmas
            return HeptagonNumber( a+d, b+e, c+f )
        elif isinstance( rhs, int ):
            return HeptagonNumber( a+rhs, b, c )
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))

    def __sub__( self, rhs ):  #self and rhs are HeptagonNumber objects
        a,b,c = self.ones, self.rhos, self.sigmas
        if isinstance( rhs, self.__class__ ):
            d,e,f = rhs.ones, rhs.rhos, rhs.sigmas
            return HeptagonNumber( a-d, b-e, c-f )
        elif isinstance( rhs, int ):
            return HeptagonNumber( a-rhs, b, c )
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))

    def __neg__( self ) :
        return HeptagonNumber( -self.ones, -self.rhos, -self.sigmas )

    def __mul__( self, rhs ) :
        a,b,c = self.ones, self.rhos, self.sigmas
        if isinstance( rhs, self.__class__ ):
            d,e,f = rhs.ones, rhs.rhos, rhs.sigmas
            return HeptagonNumber( a*d + b*e + c*f,
             a*e + b*d + b*f + c*e + c*f,
             a*f + b*e + b*f + c*d + c*e + c*f )
        elif isinstance( rhs, int ):
            return HeptagonNumber( a*rhs, b*rhs, c*rhs )
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))

    def __str__( self ):
        s = u""
        if self.ones==0 and self.rhos==0 and self.sigmas==0 :
            s = u"0"
        if self.ones != 0 :
            s = s + u"%d" % ( self.ones )
        if self.rhos != 0 :
            if len(s) > 0 :
                s = s + u"+"
            if self.rhos != 1 :
                s = s + u"%d" % ( self.rhos )
            s = s + u"\u03C1"
        if self.sigmas != 0 :
            if len(s) > 0 :
                s = s + u"+"
            if self.sigmas != 1 :
                s = s + u"%d" % ( self.sigmas )
            s = s + u"\u03C3"
        return s.encode('utf-8') 

    # These values will be derived in Part 2
    
    sigma_real = 1 / (2* math.sin(math.pi/14))

    rho_real = 2*math.sin(5*math.pi/14)

    def __float__( self ) :
        return self.ones + self.rho_real * self.rhos + self.sigma_real * self.sigmas

zero = HeptagonNumber()
one = HeptagonNumber(1)
rho = HeptagonNumber(0,1)
sigma = HeptagonNumber(0,0,1)

# Now we can use natural operators for arithmetic,
#  as long as we put integers on the right.
sigma_inv = sigma - rho
rho_inv = rho - sigma + 1
rho_over_sigma = rho - 1
sigma_over_rho = sigma - 1
    
