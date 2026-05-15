import numpy as np
import matplotlib.pyplot as plt

class YieldCurve:
    """
    YieldCurve represents a termm structure of zero rate and provides discount factors for valuations
    
    This class is infrastructure: all interest-rate logix should live here and be reused by other modles
    """
    def __init__(self, maturities, zero_rates, compounding = "continuous"):
        """
        DEFINE ALL PARAMETERS (maturities, zero_rates, compounding) IN THE CONSTRUCTOR
        compounding is either continuous or annual
        """
        self.maturities = np.array(maturities, dtype=float)
        self.zero_rates = np.array(zero_rates, dtype=float)
        self.compounding = compounding

        if len(self.maturities) != len(self.zero_rates):
            raise ValueError("Maturities and zero rates must have the same length.")
        
        order = np.argsort(self.maturities)
        self.times = self.maturities[order]
        self.zero_rates = self.zero_rates[order]

    def get_zero_rate(self, T):
        """
        Return the interpolated xero rate for maturity T (years)
        """
        T = float(T)
        return float(np.interp(T, self.maturities, self.zero_rates))
        
    def get_discount_factor(self, T):
        """
        Return the discount factor D(t) using the yield curve.
        """
        z = self.get_zero_rate(T)

        if self.compounding == "continuous":
             return np.exp(-z * T)
        elif self.compounding == "annual":
            return 1.0 / (1.0 + z) ** T
        else:
            raise ValueError("Unsupported compounding method. Use 'continuous' or 'annual'.")

    def plot(self, max_maturity = None):
        """
        Plot the yield curve up to max_maturity (years)
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

        plt.figure()
        plt.plot(T_grid, z_grid)
        plt.xlabel("Maturity (years)")
        plt.ylabel("Zero Rate")
        plt.title("Yield Curve")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
