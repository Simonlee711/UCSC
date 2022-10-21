#!/usr/bin/env python3 
# Name: Simon Lee
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

'''
Program docstring goes here
'''

import math
import re
class Triad :
    """
    Calculate angles and distances among a triad of points.
 
    Author: David Bernick
    Date: March 21, 2013
    Points can be supplied in any dimensional space as long as they are consistent.
    Points are supplied as tupels in n-dimensions, and there should be three
    of those to make the triad. Each point is positionally named as p,q,r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()
 
    Required Modules: math
    initialized: 3 positional tuples representing Points in n-space
             p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods:  angleP(), angleR(), angleQ() angles measured in radians
          dPQ(), dPR(), dQR() distances in the same units of p,q,r
 
    """
 
    def __init__(self,p,q,r) :
        """ Construct a Triad. 
        
        Example construction:
            p1 = Triad( p=(1.,0.,0.), q=(0.,0.,0.), r=(0.,0.,0.) ). 
        """
        self.p = p
        self.q = q
        self.r = r
# private helper methods
    def d2 (self,a,b) : # calculate squared distance of point a to b
        return float(sum((ia-ib)*(ia-ib)  for  ia,ib in zip (a,b)))
    
    def dot (self,a,b) : # dotProd of standard vectors a,b
        return float(sum(ia*ib for ia,ib in zip(a,b)))
    
    def ndot (self,a,b,c) : # dotProd of vec. a,c standardized to b
        return float(sum((ia-ib)*(ic-ib) for ia,ib,ic in zip (a,b,c)))
    
# calculate lengths(distances) of segments PQ, PR and QR
    def dPQ (self):
        """ Provides the distance between point p and point q """
        return math.sqrt(self.d2(self.p,self.q))
    
    def dPR (self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.d2(self.p,self.r))
    
    def dQR (self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.d2(self.q,self.r))
    
    def angleP (self) :
        """ Provides the angle made at point p by segments pq and pr (radians). """
        return math.acos(self.ndot(self.q,self.p,self.r) /   math.sqrt(self.d2(self.q,self.p)*self.d2(self.r,self.p)))
    
    def angleQ (self) :
        """ Provides the angle made at point q by segments qp and qr (radians). """
        return math.acos(self.ndot(self.p,self.q,self.r) /  math.sqrt(self.d2(self.p,self.q)*self.d2(self.r,self.q)))
 
    def angleR (self) :
        """ Provides the angle made at point r by segments rp and rq (radians). """
        return math.acos(self.ndot(self.p,self.r,self.q) /  math.sqrt(self.d2(self.p,self.r)*self.d2(self.q,self.r)))

    
def setUp(coordinates):
    '''
    Parses just the coordinates of the input
    
    i.e.
    
    C = (39.447, 94.657, 11.824) N = (39.292, 95.716, 11.027) Ca = (39.462, 97.101, 11.465)
                                            |
                                            v
    ['39.447', '94.657', '11.824', '39.292', '95.716', '11.027', '39.462', '97.101', '11.465']
    '''
    
    coord_list = re.findall("\d+\.\d+", coordinates) # use regex to extract numbers from input
    
    # index slicing to make coordinates
    p = (float(coord_list[0]), float(coord_list[1]), float(coord_list[2]))
    q = (float(coord_list[3]), float(coord_list[4]), float(coord_list[5]))
    r = (float(coord_list[6]), float(coord_list[7]), float(coord_list[8]))
    
    return p,q,r
    
def main():
    ''' Main Driver for the coordinateMathSoln code'''
    coord = input("Enter Coordinates (All in one line/sequence)")
    p,q,r = setUp(coord)
    
    triad = Triad(p, q, r)
    
    print("N-C bond length =",round(triad.dPQ(), 2))
    print("N-Ca bond length =",round(triad.dQR(),2))
    print("C-N-Ca angle length =",round(math.degrees(triad.angleQ()), 2)) # the desired output wants it in degrees.

main()
