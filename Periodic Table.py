from mendeleev import element

def get_atomic_number(symbol):
    return element(symbol).atomic_number

def get_name(symbol):
    return element(symbol).name

def get_atomic_mass(symbol):
    return element(symbol).atomic_weight

def get_atomic_radius(symbol):
    return element(symbol).atomic_radius

def get_electronegativity(symbol):
    return element(symbol).en_pauling

def get_melting_point(symbol):
    return element(symbol).melting_point

def get_boiling_point(symbol):
    return element(symbol).boiling_point

def is_metal(symbol):
    return element(symbol=symbol).is_metal

def is_noble_gas(symbol):
    return element(symbol=symbol).is_noble_gas

print(get_atomic_number('H'))  # Output: 1
print(get_name('O'))  # Output: Oxygen
print(get_atomic_radius('Na'))  # Output: 186.0
print(get_electronegativity('Cl'))  # Output: 3.16
print(get_melting_point('Cu'))  # Output: 1357.77
print(get_boiling_point('Hg'))  # Output: 629.88
