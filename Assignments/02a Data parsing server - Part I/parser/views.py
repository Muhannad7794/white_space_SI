from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import DataSerializer
from pathlib import Path
import json
import csv
import yaml
import os
import xml.etree.ElementTree as ET


# Base directory for data files
DATA_FILES_DIR = Path(__file__).resolve().parent / "data_files"


class BaseDataViewSet(viewsets.ViewSet):
    """
    A base viewset for reading and parsing data from files.
    """

    def list(self, request):
        # Placeholder for parsing logic specific to each file format
        parsed_data = self.parse_data()

        # Serializing the parsed data
        serializer = DataSerializer(parsed_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def parse_data(self):
        # Placeholder method to be overridden in subclass viewsets
        raise NotImplementedError("Subclasses must implement parse_data method")


class JsonDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.json"
        with open(file_path, "r") as file:
            return json.load(file)


class CsvDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.csv"
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


class YamlDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.yml"
        with open(file_path, "r") as file:
            return yaml.safe_load(file)


class XmlDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.xml"
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


class TxtDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.txt"
        parsed_data = {}
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
