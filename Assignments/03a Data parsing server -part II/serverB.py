from fastapi import FastAPI
import csv
import os
import requests
import xml.etree.ElementTree as ET
import json


# define the path of the data files from the data_files directory
data_path = os.path.join(os.path.dirname(__file__), "data_files")

# initialize the FastAPI app
app = FastAPI()


# parse and serve the CSV data
@app.get("/fast_parser/csv/")
async def read_csv():
    with open(os.path.join(data_path, "anna.csv"), "r") as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]


# parse and serve the XML data
@app.get("/fast_parser/xml/")
async def read_xml():
    try:
        # Read the contents of the XML file
        with open(os.path.join(data_path, "anna.xml"), "r") as file:
            xml_content = file.read()
        print("XML content:", xml_content)  # Print the contents of the XML file

        # Parse the XML content
        root = ET.fromstring(xml_content)
        data = []
        person_data = {}
        for element in root:
            if element.tag == "Hobbies":
                hobbies = [hobby.text for hobby in element.findall("Hobby")]
                person_data[element.tag] = hobbies
            else:
                person_data[element.tag] = element.text
        data.append(person_data)

        print("Parsed data:", data)  # Add this line for debugging
        return data
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        raise HTTPException(status_code=500, detail="Internal Server Error")


# parse  json data from server A
@app.get("/fast_parser/server_a/json/")
async def read_json_from_server_a():
    response = requests.get("http://localhost:8000/parser/data/json/")
    response.raise_for_status()
    return response.json()


# parse  yaml data from server A
@app.get("/fast_parser/server_a/yaml/")
async def read_yaml_from_server_a():
    response = requests.get("http://localhost:8000/parser/data/yaml/")
    response.raise_for_status()
    return response.json()
