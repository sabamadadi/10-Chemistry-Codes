from mendeleev import element

# Get the atomic number of an element
def get_atomic_number(symbol):
    return element(symbol).atomic_number

# Get the name of an element by its symbol
def get_name(symbol):
    return element(symbol).name

# Get the atomic mass of an element
def get_atomic_mass(symbol):
    return element(symbol).atomic_weight
# Get the atomic radius of an element in picometers (pm)
def get_atomic_radius(symbol):
    return element(symbol).atomic_radius

# Get the electronegativity of an element (Pauling scale)
def get_electronegativity(symbol):
    return element(symbol).en_pauling

# Get the melting point of an element in Kelvin (K)
def get_melting_point(symbol):
    return element(symbol).melting_point

# Get the boiling point of an element in Kelvin (K)
def get_boiling_point(symbol):
    return element(symbol).boiling_point

# Check if an element is a metal
def is_metal(symbol):
    return element(symbol=symbol).is_metal

# Check if an element is a noble gas
def is_noble_gas(symbol):
    return element(symbol=symbol).is_noble_gas

# Example usage
print(get_atomic_number('H'))  # Output: 1
print(get_name('O'))  # Output: Oxygen
print(get_atomic_radius('Na'))  # Output: 186.0
print(get_electronegativity('Cl'))  # Output: 3.16
print(get_melting_point('Cu'))  # Output: 1357.77
print(get_boiling_point('Hg'))  # Output: 629.88

