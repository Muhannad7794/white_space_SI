import xml.etree.ElementTree as ET

# Path to the XML file
file_path = "data_files/anna.xml"

# Parse the XML file
tree = ET.parse(file_path)
root = tree.getroot()

# Extract and print the name and age
name = root.find("Name").text
age = root.find("Age").text

# Extract the hobbies
hobbies_elements = root.find("Hobbies").findall("Hobby")
hobbies = [hobby.text for hobby in hobbies_elements]

# Join the list of hobbies into a single string with commas
hobbies_str = ", ".join(hobbies)

print(name)
print(age)
print(hobbies_str)
