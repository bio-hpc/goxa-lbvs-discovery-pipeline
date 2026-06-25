import pandas as pd
import glob

# Define the path to your files and the output file
input_files_pattern = 'REAL_Enamine/filter250/*.tsv'  # Adjust this pattern to match your files
output_file = 'REAL_Enamine_250.tsv'

# Get the list of all files matching the pattern
files = glob.glob(input_files_pattern)

# Initialize an empty list to store dataframes
dfs = []

for i, file in enumerate(files):
    # Read each file into a dataframe
    df = pd.read_csv(file, delimiter='\t')  # Adjust the delimiter if needed
    print(file)
    print(df)
    if i == 0:
        # For the first file, include the header
        dfs.append(df)
    else:
        # For other files, skip the header
        dfs.append(df[1:])

# Concatenate all dataframes
merged_df = pd.concat(dfs, ignore_index=True)
print(merged_df[['smiles','idnumber']])
# Write the merged dataframe to a new file
merged_df[['smiles','idnumber']].to_csv(output_file, index=False, sep='\t')
