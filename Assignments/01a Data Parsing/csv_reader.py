import csv

# refrence the file path
file_path = "data_files/anna.csv"

# open the CSV file for reading
with open(file_path, "r") as file:
    # parse the CSV file as a string
    csv_file = csv.reader(file)

    # Skip the header row
    next(csv_file, None)

    # iterate through the CSV file
    for row in csv_file:
        name = row[0]
        age = row[1]
        hobbies = row[2]
    

        # Print the parsed data
        print(name)
        print(age)
        print(hobbies)
