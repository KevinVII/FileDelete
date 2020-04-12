import os
from os import listdir

# Get directory and extensions to delete
folder_path = input("Enter directory: ")
extension = input("Extensions to delete: ")

if not folder_path.endswith("\\"):
    folder_path = folder_path + "\\"

# Iterate through files and delete those with given extension
for file_name in listdir(folder_path):
    if file_name.endswith(extension):
        os.remove(folder_path + file_name)
