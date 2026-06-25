import pandas as pd

# Define the chunk size
chunk_size = 500000
file_counter = 0

# Open the original TSV file
with pd.read_csv('REAL_Enamine_HAC_6_21.tsv', sep='\t', chunksize=chunk_size) as reader:
    for chunk in reader:
        # Define the output file name
        output_file = f'REAL_Enamine_HAC_6_21_{file_counter}.tsv'
        # Save the chunk to a new TSV file
        chunk.to_csv(output_file, sep='\t', index=False)
        file_counter += 1
