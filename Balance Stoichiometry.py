from chempy import balance_stoichiometry
from chempy import Substance

acid = Substance('HCl')
metal = Substance('Zn')

balanced_reaction = balance_stoichiometry({str(acid), str(metal)}, {'H2', 'ZnCl2'})

for reactant, coefficient in balanced_reaction[0].items():
    print(f"{coefficient} {reactant} + ", end='')
print(" -> ", end='')
for product, coefficient in balanced_reaction[1].items():
    print(f"{coefficient} {product} + ", end='')
