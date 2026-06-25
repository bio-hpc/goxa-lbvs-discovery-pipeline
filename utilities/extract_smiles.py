import pandas as pd
import sys

def filter_and_extract_data(file_name):
    # Read the TSV data from the input file with low_memory set to False to avoid DtypeWarning
    df = pd.read_csv(file_name, sep='\t', low_memory=False)
    # print(df)
    # print(df)
    # print('Detected')
    # Filter the DataFrame for rows where MW < 120
    filtered_df = df[df['MW'] < 250]

    # Extract the SMILES and idnumber columns from the filtered DataFrame
    extracted_df = filtered_df[['smiles', 'idnumber']]

    # Display the extracted data
    if len(extracted_df) != 0:
        print(extracted_df)
        extracted_df.to_csv(output_file, sep='\t')
    # Optionally, save the extracted data to a new TSV file
    # 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_tsv_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        filter_and_extract_data(input_file)


