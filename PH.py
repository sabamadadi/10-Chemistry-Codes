# Function to calculate the pH of a solution
import math


def calculate_pH(hydrogen_concentration):
    pH = -1 * (math.log10(hydrogen_concentration))
    return pH

# Example usage
hydrogen_concentration = 1.0e-7  # Concentration of hydrogen ions in moles per liter (pH 7 represents neutral solution)
pH = calculate_pH(hydrogen_concentration)

print(f"The pH of the solution is: {pH}")
