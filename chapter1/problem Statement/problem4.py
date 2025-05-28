import os

# Specify the path (you can change it to any directory)
path = "."

# List all files and directories
contents = os.listdir(path)

print(f"Contents of directory '{os.path.abspath(path)}':")
for item in contents:
    print(item)
