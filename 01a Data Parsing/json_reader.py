import json

# Path to your JSON file
file_path = "data_files/anna.json"

# Open the JSON file for reading
with open(file_path, "r") as file:
    # Parse the JSON file into a Python dictionary
    data = json.load(file)

first_person = data[0]

# print the first person details as a string
print(first_person["name"])
print(first_person["age"])
# convert the hobbies list into a string:
hobbies = ", ".join(first_person["hobbies"])
print(hobbies)
