from rdkit import Chem

smiles = "CCOCC(=O)N"

molecule = Chem.MolFromSmiles(smiles)

bond_count = molecule.GetNumBonds()

print("Number of bonds in the organic compound:", bond_count)
