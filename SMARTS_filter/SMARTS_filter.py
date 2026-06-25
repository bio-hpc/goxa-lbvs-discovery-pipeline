import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

# Function to check the molecular weight
def check_molecular_weight(mol, max_weight):
    return AllChem.CalcExactMolWt(mol) <= max_weight

# Function to check for primary amine
def has_primary_amine(mol):
    primary_amine_smarts = '[NH2]'
    pattern = Chem.MolFromSmarts(primary_amine_smarts)
    return mol.HasSubstructMatch(pattern)

# Function to check for specific conditions around the primary amine
def check_conditions(mol):
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() == 7 and atom.GetDegree() == 1:  # Primary amine check
            neighbor = atom.GetNeighbors()[0]  # Get the neighbor atom of the nitrogen
            neighbor_degree = neighbor.GetDegree() - 1  # Degree excluding the primary amine
            allowed_atomic_nums = {7, 8, 9, 17, 53}  # N, O, F, Cl, I
            
            if neighbor_degree == 1 and neighbor.GetSymbol() == 'C':  # If the neighbor has exactly 1 other neighbor
                second_level_neighbors = neighbor.GetNeighbors()
                second_level_neighbors = [n for n in second_level_neighbors if n.GetIdx() != atom.GetIdx()]
                if len(second_level_neighbors) == 1 and second_level_neighbors[0].GetSymbol() == 'C':
                    third_level_neighbors=second_level_neighbors[0].GetNeighbors()
                    if len(third_level_neighbors) == 3:
                        number_carbon = 0         # Save the number of neighbor carbon of the second_level_carbon
                        number_hb_enabler = 0     # Save the number of neighbor atoms of the second_level_carbon able to form Hbonds
                        number_coord_enabler = 0  # Save the number of neighbor atoms of the second_level_carbon able to coordinate Hys
                        for i in third_level_neighbors:
                            if i.GetSymbol() == 'C':
                                number_carbon+=1
                            if i.GetSymbol() in {'N','F','O','Cl','I'} and number_hb_enabler == 0:
                                number_hb_enabler+=1
                            elif i.GetSymbol() in {'N','O'}:
                                number_coord_enabler+=1
                        #print('CORRECT',number_carbon)
                        if number_carbon <= 1 and number_coord_enabler >= 1 and number_hb_enabler == 1 and number_coord_enabler >= 1:
                            return True
            elif neighbor_degree == 2:  # If the neighbor has exactly 2 other neighbors
                second_level_neighbors = neighbor.GetNeighbors()
                # Ensure the second-level neighbors are not the primary amine
                second_level_neighbors = [n for n in second_level_neighbors if n.GetIdx() != atom.GetIdx()]
                # Check if both second-level neighbors are among the allowed atoms
                if len(second_level_neighbors) == 2 and all(
                    n.GetAtomicNum() in allowed_atomic_nums and n.GetDegree() == 1 for n in second_level_neighbors
                ):
                    return True
    return False

# Main function to check if a SMILES string meets the requirements
def check_smiles(smiles, max_weight=200):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    if not check_molecular_weight(mol, max_weight):
        return False
    if not has_primary_amine(mol):
        return False
    if not check_conditions(mol):
        return False
    # print(smiles)
    return True

# Function to process the CSV file
def process_csv(file_path):
    df = pd.read_csv(file_path, sep='\t', header=None, names=['SMILES', 'Identifier'])
    df['Meets_Criteria'] = df['SMILES'].apply(check_smiles)
    return df[df['Meets_Criteria']]

# Example usage
file_path = "REAL_Enamine_250.tsv"
filtered_df = process_csv(file_path)
filtered_df.to_csv("Filtered_REAL_Enamine_250.csv", index=False)

# # Display the filtered DataFrame
# print(filtered_df)
for i in filtered_df['SMILES']:
    print(i)

