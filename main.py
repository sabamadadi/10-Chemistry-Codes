#balance
from chempy import balance_stoichiometry
from chempy import Substance

# Define the acid and metal substances
acid = Substance('HCl')
metal = Substance('Zn')

# Balance the reaction equation
balanced_reaction = balance_stoichiometry({str(acid), str(metal)}, {'H2', 'ZnCl2'})

# Print the balanced reaction equation
for reactant, coefficient in balanced_reaction[0].items():
    print(f"{coefficient} {reactant} + ", end='')
print(" -> ", end='')
for product, coefficient in balanced_reaction[1].items():
    print(f"{coefficient} {product} + ", end='')
from chempy import balance_stoichiometry
from chempy import Substance

# Define the acid and metal substances
acid = Substance('HCl')
metal = Substance('Zn')

# Balance the reaction equation
balanced_reaction = balance_stoichiometry({str(acid), str(metal)}, {'H2', 'ZnCl2'})

# Print the balanced reaction equation
for reactant, coefficient in balanced_reaction[0].items():
    print(f"{coefficient} {reactant} + ", end='')
print(" -> ", end='')
for product, coefficient in balanced_reaction[1].items():
    print(f"{coefficient} {product} + ", end='')