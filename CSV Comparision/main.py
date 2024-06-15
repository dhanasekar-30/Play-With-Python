import csv
import os
from config import *

# Get the list of CSV files in each folder
folder1_files = [f for f in os.listdir(folder1_path) if f.endswith('.csv')]
folder2_files = [f for f in os.listdir(folder2_path) if f.endswith('.csv')]

# Sort the file lists to ensure consistent order for comparison
folder1_files.sort()
folder2_files.sort()

# Iterate over each pair of files and compare their contents
for file1, file2 in zip(folder1_files, folder2_files):
    file1_path = os.path.join(folder1_path, file1)
    file2_path = os.path.join(folder2_path, file2)

    with open(file1_path, 'r') as csv_file1, open(file2_path, 'r') as csv_file2:
        reader1 = csv.reader(csv_file1)
        reader2 = csv.reader(csv_file2)

        # Read the rows of each file
        rows1 = [row for row in reader1 if row]
        rows2 = [row for row in reader2 if row]

        if rows1 == rows2:
            print(f'True: {file1} matches {file2}')
        else:
            print(f'False: {file1} does not match {file2}')