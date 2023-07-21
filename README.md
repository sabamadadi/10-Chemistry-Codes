# 10 Chemistry Codes ✅

Final project for Mathematical Software 2 course at Shahid Beheshti University (Spring 2023)

Score: 9 out of 10

Course Instructor: [Alireza Afzal Aghaei](https://github.com/alirezaafzalaghaei)

## 3D
This code creates a 3D visualization of a water molecule using the Matplotlib library. The coordinates of the atoms in the water molecule are defined, including the oxygen atom and two hydrogen atoms. The code then creates a 3D plot using the specified coordinates, and uses the `scatter` function to plot each atom as a single point in 3D space. The atoms are colored differently to differentiate between the oxygen and hydrogen atoms.

The code then uses the `plot` function to connect the atoms with lines to form the water molecule. The lines connecting the atoms are colored black to represent chemical bonds between the atoms.

The axis labels are set using the `set_xlabel`, `set_ylabel`, and `set_zlabel` functions, and the plot limits are set using the `set_xlim`, `set_ylim`, and `set_zlim` functions to ensure that the molecule is centered in the plot.

Finally, a legend is added to the plot using the `legend` function, and the plot is displayed using the `show` function. The resulting plot shows a 3D representation of a water molecule, with the oxygen atom at the center and the two hydrogen atoms bonded to it.

## Atomic Model Changes
This code creates a simple line plot using the Matplotlib library to show the evolution of atomic models over time. The plot shows the relationship between the year in which the model was proposed and the estimated atomic radius according to each model.

First, the code defines three lists: `models`, `years`, and `radii`. These lists contain the names of the atomic models, the years in which they were proposed, and the estimated atomic radii according to each model, respectively.

Next, a figure and axis are created using the `subplots` function. The code then plots the `years` and `radii` lists as a line graph using the `plot` function, with markers at each data point to indicate the model.

The code then sets the x-axis label, y-axis label, and title of the plot using the `set_xlabel`, `set_ylabel`, and `set_title` functions, respectively.

Finally, the code uses a `for` loop and the `annotate` function to add labels to each data point on the plot, showing the name of the corresponding atomic model. The resulting plot shows the evolution of atomic models over time, with each model represented by a data point on the graph and labeled with its name.

## Atomic Radius Changes
This code creates a simple line plot using the Matplotlib library to show the relationship between atomic number and atomic radius in the periodic table.

The code defines two lists: `atomic_numbers` and `atomic_radii`. The `atomic_numbers` list contains the atomic numbers of several elements, while the `atomic_radii` list contains the corresponding atomic radii in Angstroms.

Next, the code plots the `atomic_numbers` and `atomic_radii` lists as a line graph using the `plot` function, with markers at each data point to indicate the element. The line is blue, and solid.

The code then sets the title, x-axis label, and y-axis label of the plot using the `title`, `xlabel`, and `ylabel` functions, respectively. Additionally, the `grid` function is used to add grid lines to the plot.

Finally, the plot is displayed using the `show` function. The resulting plot shows the trend of atomic radii across the periodic table, with a gradual increase in radius from left to right. The markers on the plot indicate the corresponding atomic number of each element.

## Balance Stoichiometry
This code balances a chemical equation between an acid (HCl) and a metal (Zn) using the `balance_stoichiometry` function from the `chempy` library. The balanced equation is then printed to the console.

First, the code initializes two `Substance` objects to represent the acid and metal. Next, the `balance_stoichiometry` function is called with a set of reactants (the acid and metal) and a set of products (hydrogen gas and zinc chloride). The function returns a tuple of two dictionaries, representing the coefficients of the reactants and products in the balanced equation.

Finally, the code prints the balanced equation to the console using a `for` loop to iterate over the reactants and products dictionaries, printing the coefficients and substance names for each. The result is a balanced chemical equation that shows the stoichiometric relationship between the acid and metal, and the products that are formed as a result of their reaction.

## Bohr's Atomic Model
This code creates a simple visualization of an atom using the Matplotlib library. The visualization consists of a nucleus and several electrons orbiting around it.

First, the code defines several constants, including the radii of the nucleus and electrons, and the radii and colors of the electron orbits. Next, a figure and axis are created using the `subplots` function.

The code then plots the nucleus as a black circle using the `Circle` function, and adds it to the axis using the `add_artist` function. Similarly, the electron orbits are plotted as circles with the specified radii and colors, and added to the axis.

Next, the code calculates the positions of the electrons using polar coordinates, and plots them as smaller black circles using the `Circle` function. Finally, the aspect ratio and limits of the plot are set, ticks and labels are removed from the axis, and the plot is displayed using the `show` function.

The resulting plot shows a simple model of an atom, with the nucleus at the center and several electrons orbiting around it in circular orbits. The radii of the orbits increase with distance from the nucleus, and the electrons are evenly spaced around each orbit.

## Molar Mass
This code defines a function `calculate_molar_mass` that calculates the molar mass of a compound based on its chemical formula. The function takes a single argument `compound`, which is a dictionary representing the elements and their respective counts in the compound. The `atomic_masses` dictionary provides the atomic masses of the relevant elements.

The code then provides an example usage of the `calculate_molar_mass` function by setting the `compound` variable to a dictionary representing the chemical formula for methane (CH4), and calling the `calculate_molar_mass` function with this dictionary. The resulting molar mass is then printed to the console using a formatted string.

Overall, this code provides a simple way to calculate the molar mass of a compound based on its chemical formula, and demonstrates how to use dictionaries and loops in Python to perform mathematical calculations.

## Organic Compound
This code uses the `rdkit` library to calculate the number of bonds in an organic compound represented by a SMILES string.

First, the SMILES string is defined as `CCOCC(=O)N`. Next, the `MolFromSmiles` function from the `Chem` module of the `rdkit` library is called with this SMILES string as an argument. This function returns a `Mol` object representing the molecule.

The `GetNumBonds` method is then called on the `Mol` object to count the number of bonds in the molecule. The result is assigned to the `bond_count` variable.

Finally, the code prints a message to the console indicating the number of bonds in the organic compound, using the `print` function and a formatted string to insert the `bond_count` variable into the message.

Overall, this code demonstrates how to use the `rdkit` library to parse a SMILES string and count the number of bonds in the resulting molecule.

## PH
This code defines a function `calculate_pH` that calculates the pH of a solution based on its hydrogen ion concentration. The function takes a single argument `hydrogen_concentration`, which represents the concentration of hydrogen ions in moles per liter. The function returns the pH of the solution, which is calculated as the negative base-10 logarithm of the hydrogen ion concentration.

The code then provides an example usage of the `calculate_pH` function by setting the `hydrogen_concentration` variable to a value of 1.0e-7 (which corresponds to a neutral solution with a pH of 7), and calling the `calculate_pH` function with this value. The resulting pH is then printed to the console using a formatted string.

Overall, this code provides a simple way to calculate the pH of a solution based on its hydrogen ion concentration, and demonstrates how to use the `math` library in Python to perform logarithmic calculations.

## Periodic Table
This code uses the `mendeleev` library to obtain various properties of chemical elements.

The code defines several functions, each of which takes a chemical element symbol as an argument and returns a specific property of the element:

- `get_atomic_number` returns the atomic number of the element.
- `get_name` returns the name of the element.
- `get_atomic_mass` returns the atomic mass of the element.
- `get_atomic_radius` returns the atomic radius of the element.
- `get_electronegativity` returns the electronegativity of the element.
- `get_melting_point` returns the melting point of the element.
- `get_boiling_point` returns the boiling point of the element.
- `is_metal` returns `True` if the element is a metal, and `False` otherwise.
- `is_noble_gas` returns `True` if the element is a noble gas, and `False` otherwise.

The code then provides example usages of these functions by calling them with various element symbols and printing the resulting properties to the console.

Overall, this code demonstrates how to use the `mendeleev` library to obtain a variety of properties of chemical elements in Python.

## Stoichiometric Equation
The code performs two calculations: the first calculates the number of moles of H2O produced from 26.0 g of H2O2, and the second calculates the number of molecules of I2 produced and the mass of I2 produced from the reaction of 0.4235 mol of CuCl2 with 4KI.

For the first calculation, the code uses the molar mass of H2O2 (34.0147 g/mol) to convert the given mass of H2O2 to moles. It then uses the stoichiometric coefficients from the balanced equation to calculate the moles of H2O produced from the moles of H2O2. Finally, it prints the result to the console.

For the second calculation, the code uses the stoichiometric coefficients from the balanced equation to calculate the moles of I2 produced from the given moles of CuCl2. It then uses Avogadro's number to convert the moles of I2 to molecules, and the molar mass of I2 (253.8089 g/mol) to calculate the mass of I2 produced. Finally, it prints the number of molecules of I2 produced and the mass of I2 produced to the console.

Overall, this code demonstrates how to perform stoichiometric calculations in chemistry using Python, including converting between mass and moles, calculating the number of molecules, and using stoichiometric coefficients to relate the amounts of reactants and products in a chemical reaction.
