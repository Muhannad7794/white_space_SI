# Path to the text file
file_path = "data_files/anna.txt"

# Initialize a dictionary to hold the parsed data
parsed_data = {}

# Open and read the text file
with open(file_path, "r") as file:
    for line in file:
        # Split each line into key and value parts
        key, value = line.strip().split(": ", 1)
        # Trim any leading/trailing whitespace and store in dictionary
        parsed_data[key.strip()] = value.strip()

# Extract and print the parsed data
print(parsed_data["name"])
print(parsed_data["age"])
print(parsed_data["hobbies"])
