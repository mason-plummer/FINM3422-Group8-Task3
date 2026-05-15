import numpy as np 
import matplotlib.pyplot as plt

class YieldCurve:
    """
    YieldCurve represents a term structure of zero rates and provides discount factors for valuations. 
    
    """
    def __init__(self, maturities, zero_rates, compounding = "continuous"):
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

    def plot(self, max_maturity = None):
        """
        Plot the yield curve up to a specified maximum maturity. If max_maturity is None, it will plot up to the maximum maturity in the curve.
        """
        if max_maturity is None:
            T_grid = self.maturities

        else:
            T_grid = np.linspace(
                self.maturities.min(),
                max_maturity,
                100
            )

        z_grid = [self.get_zero_rate(T) for T in T_grid]

        # T gives all our x values, z grid gives all our y values, and then we can plot them using matplotlib.

        plt.figure()
        plt.plot(T_grid, z_grid)
        plt.xlabel("Maturity (years)")
        plt.ylabel("Zero Rate")
        plt.title("Figure 1: Yield Curve")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
