# calculate the number of moles of H2O produced from 26.0 g of H2O2

# Step 1: Convert mass of H2O2 to moles
molar_mass_h2o2 = 34.0147  # g/mol
mass_h2o2 = 26.0  # g
moles_h2o2 = mass_h2o2 / molar_mass_h2o2

# Step 2: Calculate moles of H2O produced based on stoichiometry
stoichiometric_coefficient_h2o2 = 2
stoichiometric_coefficient_h2o = 2
moles_h2o = (moles_h2o2 * stoichiometric_coefficient_h2o) / stoichiometric_coefficient_h2o2

# Step 3: Print the result
print("Moles of H2O produced:", moles_h2o)


# I2 is produced by the reaction of 0.4235 mol of CuCl2 according to the following equation:  2CuCl2+4KI→2CuI+4KCl+I2
# How many molecules of I2 are produced?
# What mass of I2 is produced?

# Step 1: Calculate moles of I2 produced based on stoichiometry
moles_cucl2 = 0.4235
stoichiometric_coefficient_cucl2 = 2
stoichiometric_coefficient_i2 = 1
moles_i2 = (moles_cucl2 * stoichiometric_coefficient_i2) / stoichiometric_coefficient_cucl2

# Step 2: Convert moles of I2 to molecules
avogadro_number = 6.02214076e23
molecules_i2 = moles_i2 * avogadro_number

# Step 3: Calculate mass of I2 produced
molar_mass_i2 = 253.8089  # g/mol
mass_i2 = moles_i2 * molar_mass_i2

# Step 4: Print the results
print("Number of molecules of I2 produced:", molecules_i2)
print("Mass of I2 produced:", mass_i2, "g")
