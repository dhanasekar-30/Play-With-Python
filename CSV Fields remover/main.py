import os
import pandas as pd

folder_path = 'path/to/csv/folder/'
elements_to_remove = ['Dd', 'Ee']
# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Iterate over each CSV file
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Remove the 'Dd' and 'Ee' columns
    df = df.drop(elements_to_remove, axis=1)
    
    # Save the modified DataFrame back to the CSV file
    df.to_csv(file_path, index=False)