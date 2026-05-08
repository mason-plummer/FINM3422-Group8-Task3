import numpy as np 
import matplotlib.pyplot as plt

class YieldCurve:
    """
    YieldCurve represents a term structure of zero rates and provides discount factors for valuations. 
    
    """
    def __init__(self, maturities, zero_rates, compounding = "coninuous"):
        """
        Maturies are the time to maturity for each zero rate, and zero_rates are the corresponding zero rates - for reference these will be entered in as lists. The compounding method can be "continuous" or "annual" and will be entered using strings.
        """

        self.maturities = np.array(maturities, dtype=float)
        self.zero_rates = np.array(zero_rates, dtype=float)
        # want these to be numpy arrays for easier calculations and to ensure they are floats for the discount factor calculations.
        self.compounding = compounding
        # keep it as a string for the discount factor calculations, but could also be an enum or something else if we wanted to be more robust.

        if len(self.maturities) != len(self.zero_rates):
            raise ValueError("Maturities and zero rates must have the same length.")
        
        order = np.argsort(self.maturities)
        # numpy function to sor the maturities and zero rates in ascending order of maturities, which is important for interpolation and discount factor calculations.
        self.maturities = self.maturities[order]
        self.zero_rates = self.zero_rates[order]

    def get_zero_rate(self, T):
        """
        Return the interpolated zero rate for a given maturity T. 
        """
        T = float(T)
        return float(np.interp(T, self.maturities, self.zero_rates))
    
    def get_discount_factor(self, T):
        """ # doc string
        Return the discount factor D(T) using the yield curve.
        """
        z = self.get_zero_rate(T)
        # Returns the zero rate at time T 

        if self.compounding == "continuous":
            return np.exp(-z * T)
        # Discount factor under continuous compounding 
        elif self.compounding == "annual":
            return 1 / (1 + z) ** T
        # Discount factor under annual compounding
        else: # should probably be raised in __init__  
            raise ValueError("Compounding should be either 'continuous' or 'annual'.")


