import csv
from rdkit import Chem
from rdkit.Chem import Descriptors

def calculate_molecular_weight(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        return None
    return Descriptors.MolWt(molecule)

# Example usage
for i in range(1,2798):
    processed_file_path = 'REAL_Enamine_smi/PartList'+ str(i) +'.smi' 
    final_output_path = 'REAL_Enamine_size_smi/PartList_size' + str(i) + '.smi'   # Path for the new output file

    # Open the processed file and create the final output file
    with open(processed_file_path, mode='r') as infile, open(final_output_path, mode='w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        # Process each row
        for row in reader:
            if row and calculate_molecular_weight(row[0])<=150:
                print(row)
                print(calculate_molecular_weight(row[0]))
                writer.writerow(row)

    print("File processing complete.")