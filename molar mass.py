# Define the atomic masses of elements (in g/mol)
atomic_masses = {
    'H': 1.00784,
    'C': 12.0107,
    'O': 15.999,
    'N': 14.0067
}

# Function to calculate the molar mass of a compound
def calculate_molar_mass(compound):
    molar_mass = 0.0
    for element, count in compound.items():
        molar_mass += atomic_masses[element] * count
    return molar_mass

# Example usage
compound = {'H': 2, 'C': 1, 'O': 1}  # Representing the formula for methane (CH4)
molar_mass = calculate_molar_mass(compound)

print(f"The molar mass of the compound is: {molar_mass} g/mol")
