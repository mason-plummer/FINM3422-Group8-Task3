import numpy as np
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
     r = self.yield_curve.get_zero_rate(self.T) 
     
     # d1 and d2 
     d1 = (
        np.log(self.S0 / self.K) + (r + 0.5 * self.sigma ** 2) * self.T
     ) / (self.sigma * np.sqrt(self.T))
     d2 = d1 - self.sigma * np.sqrt(self.T)
     
     # Also possible to define d1, d2 here as well.

def price(self):
   return NotImplementedError("Pricing should be done within subclasses, not within the base class.")

class EuropeanCall(Derivative):
   """
   European Call option priced using black-scholes
   """

# Don't need an initialisation function as it will call the one above. 

   def price(self):
      """
      Return the black-scholes price for a european call option.
      """
      call_price = (
      self.S0 * norm.cdf(self.d1) - self.K * np.exp(-r * self.T) * norm.cdf(self.d2)
   )
      return call_price
   
