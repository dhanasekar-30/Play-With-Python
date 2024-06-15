import os
import csv

folder_path = 'D:\\Anthology\\Q2-2023'  # Replace with the actual path to your folder
output_file = 'D:\\Anthology\\q2-size.csv' # Name of the output CSV file

# Get the list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Sort the file names in ascending order
csv_files.sort()

# Create a list to store the file size information
file_sizes = []

# Iterate over the sorted file names and collect the size of each file in megabytes
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    file_size_bytes = os.path.getsize(file_path)
    file_size_mb = file_size_bytes / (1024 * 1024)  # Convert bytes to megabytes
    file_sizes.append([file_name, file_size_mb])

# Export the file size information to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Name', 'Size (MB)'])  # Write header row
    writer.writerows(file_sizes)  # Write file size data rows

print(f'File sizes exported to {output_file} successfully.')