import numpy
from scipy.stats import norm
class Derivative:
    """
    Base class for any derivative contract
    
    Class will be used for initialisation but not for any pricing
    """

    def __init__(self, S0, K, T, sigma, yield_curve):
        """
        Define all paramaters
        S0: float 
            current price of the underlying asset
        K: strike price of the option
        T: time to maturity of the option (in years)
        r: risk-free interest rate (annualised)
        sigma: volatility of the underlying asset (annualised)
        yield_curve: a function that takes time to maturity and returns the corresponding interest rate
        """
        self.S0 = S0
        self.K = K
        self.T = T
        self.sigma = sigma
        self.yield_curve = yield_curve
        # can define d1 and d2 here as they are used in both call and put options

    def price(self):
        return NotImplementedError("Price should not be done within the subclass")

class EuropeanCall(Derivative):
    """
    European Call option priced using the Black-Scholes formula
    """
    def price(self):
        """
        return the black-scholes price of a European call option
        """
        #zero-rate
        r = self.yield_curve.get_zero_rate(self.T)

        #d1 & d2
        d1 = (np.log(self.S0 / self.K) + (r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        #should do in initialisation step

        # black-scholes pricing
        call_price = self.S0 * norm.cdf(d1) - self.K * np.exp(-r * self.T) * norm.cdf(d2)
        return call_price