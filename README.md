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

## Bohr's Atomic Model
This code creates a simple visualization of an atom using the Matplotlib library. The visualization consists of a nucleus and several electrons orbiting around it.

First, the code defines several constants, including the radii of the nucleus and electrons, and the radii and colors of the electron orbits. Next, a figure and axis are created using the `subplots` function.

The code then plots the nucleus as a black circle using the `Circle` function, and adds it to the axis using the `add_artist` function. Similarly, the electron orbits are plotted as circles with the specified radii and colors, and added to the axis.

Next, the code calculates the positions of the electrons using polar coordinates, and plots them as smaller black circles using the `Circle` function. Finally, the aspect ratio and limits of the plot are set, ticks and labels are removed from the axis, and the plot is displayed using the `show` function.

The resulting plot shows a simple model of an atom, with the nucleus at the center and several electrons orbiting around it in circular orbits. The radii of the orbits increase with distance from the nucleus, and the electrons are evenly spaced around each orbit.

## PH
This code defines a function `calculate_pH` that calculates the pH of a solution based on its hydrogen ion concentration. The function takes a single argument `hydrogen_concentration`, which represents the concentration of hydrogen ions in moles per liter. The function returns the pH of the solution, which is calculated as the negative base-10 logarithm of the hydrogen ion concentration.

The code then provides an example usage of the `calculate_pH` function by setting the `hydrogen_concentration` variable to a value of 1.0e-7 (which corresponds to a neutral solution with a pH of 7), and calling the `calculate_pH` function with this value. The resulting pH is then printed to the console using a formatted string.

Overall, this code provides a simple way to calculate the pH of a solution based on its hydrogen ion concentration, and demonstrates how to use the `math` library in Python to perform logarithmic calculations.

