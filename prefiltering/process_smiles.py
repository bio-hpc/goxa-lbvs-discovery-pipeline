import csv

# File paths
for i in range(1,2798):
    input_file_path = 'REAL_Enamine_source/PartList' + str(i) + '.cxsmiles'  # Replace with your input file path
    output_file_path = 'REAL_Enamine_smi/PartList' + str(i) + '.smi'     # Replace with your desired output file path

    # Open the input file and create the output file
    with open(input_file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t') # Assuming your file is tab-delimited
        writer = csv.writer(outfile, delimiter='\t')

        # Process each row
        for row in reader:
            if row:  # Check if the row is not empty
                first_two_columns = row[:2]  # Extract the first two columns
                writer.writerow(first_two_columns)  # Write to the output file

    print("File processing complete.")
