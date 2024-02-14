import yaml

# Path to the YAML file
file_path = "data_files/anna.yml"

# Open the YAML file for reading
with open(file_path, "r") as file:
    # Load the YAML content into a Python dictionary
    data = yaml.safe_load(file)

# Print the parsed data
name = data["name"]
age = data["age"]
# Join the list of hobbies into a single string with commas
hobbies_str = ", ".join(data["hobbies"])

print(name)
print(age)
print(hobbies_str)
