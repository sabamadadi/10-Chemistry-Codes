# 10 Chemistry Problems

Final project for Mathematical Software 2 course at Shahid Beheshti University (Spring 2023)

Score: 9 out of 10

## 3D
This code creates a 3D visualization of a water molecule using the Matplotlib library. The coordinates of the atoms in the water molecule are defined, including the oxygen atom and two hydrogen atoms. The code then creates a 3D plot using the specified coordinates, and uses the `scatter` function to plot each atom as a single point in 3D space. The atoms are colored differently to differentiate between the oxygen and hydrogen atoms.

The code then uses the `plot` function to connect the atoms with lines to form the water molecule. The lines connecting the atoms are colored black to represent chemical bonds between the atoms.

The axis labels are set using the `set_xlabel`, `set_ylabel`, and `set_zlabel` functions, and the plot limits are set using the `set_xlim`, `set_ylim`, and `set_zlim` functions to ensure that the molecule is centered in the plot.

Finally, a legend is added to the plot using the `legend` function, and the plot is displayed using the `show` function. The resulting plot shows a 3D representation of a water molecule, with the oxygen atom at the center and the two hydrogen atoms bonded to it.

## Balance Stoichiometry
This code balances a chemical equation between an acid (HCl) and a metal (Zn) using the `balance_stoichiometry` function from the `chempy` library. The balanced equation is then printed to the console.

First, the code initializes two `Substance` objects to represent the acid and metal. Next, the `balance_stoichiometry` function is called with a set of reactants (the acid and metal) and a set of products (hydrogen gas and zinc chloride). The function returns a tuple of two dictionaries, representing the coefficients of the reactants and products in the balanced equation.

Finally, the code prints the balanced equation to the console using a `for` loop to iterate over the reactants and products dictionaries, printing the coefficients and substance names for each. The result is a balanced chemical equation that shows the stoichiometric relationship between the acid and metal, and the products that are formed as a result of their reaction.
