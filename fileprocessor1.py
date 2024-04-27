# Open the file
with open("fileprocessor.input", "r") as file:
    # Read each line into a list
    lines = file.readlines()

# Initialize an empty list to store parsed data
data = []

# Iterate over each line
for line in lines:
    # Skip lines that start with a hashtag
    if line.startswith('#'):
        continue
    # Split each line into a list using colon as delimiter
    line_data = line.strip().split(':')
    # Append the parsed data to the main list
    data.append(line_data)

print(data)
