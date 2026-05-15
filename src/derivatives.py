import numpy 
from scipy.stats import norm 

class Derivative: 
    """
    base class for any derivative contract 
    
    class will be used for initialisation but not for any pricing 
    
    # Re-write BETTER 

    """
    def __init__(self, S0, K, T, sigma, yield_curve): 
     """
     Define all parameters 
     e.g. 
     S0: float 
        current price of the underlying asset 
     """
     # Probably define r (the zero rate) here as well. 

     self.S0 = S0
     self.K = K
     self.T = T
     self.sigma = sigma
     self.yield_curve = yield_curve
     # Also possible to define d1, d2 here as well.

def price(self):
   return NotImplementedError("Pricing should be done within subclasses, not within the base class.")