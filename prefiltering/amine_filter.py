import csv
from rdkit import Chem

def detect_primary_amine(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    nh2_count = sum(1 for atom in mol.GetAtoms() if atom.GetAtomicNum() == 7 and atom.GetTotalNumHs() == 2)
    return nh2_count > 0

# File paths
for i in range(1,2798):
    processed_file_path = 'REAL_Enamine_size_smi/PartList_size'+ str(i) +'.smi'  # The file generated from your previous script
    final_output_path = 'REAL_Enamine_filtered_size_smi/PartList_filtered_size'+ str(i) + '.smi'   # Path for the new output file

    # Open the processed file and create the final output file
    with open(processed_file_path, mode='r') as infile, open(final_output_path, mode='w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        # Process each row
        for row in reader:
            if row and detect_primary_amine(row[0]):
                print(row)
                writer.writerow(row)

    print("File processing complete.")

