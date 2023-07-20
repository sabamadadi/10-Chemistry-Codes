from rdkit import Chem

# Define the organic compound as a SMILES string
smiles = "CCOCC(=O)N"

# Create a molecule object from the SMILES string
molecule = Chem.MolFromSmiles(smiles)

# Count the number of bonds in the molecule
bond_count = molecule.GetNumBonds()

# Print the result
print("Number of bonds in the organic compound:", bond_count)
