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
            reader = csv.DictReader(file)
            return next(reader)


class YamlDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.yaml"
        with open(file_path, "r") as file:
            return yaml.safe_load(file)


class XmlDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.xml"
        tree = ET.parse(file_path)
        root = tree.getroot()
        return {
            "name": root.find("name").text,
            "age": int(root.find("age").text),
            "hobbies": [hobby.text for hobby in root.find("hobbies")],
        }


class TxtDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.txt"
        with open(file_path, "r") as file:
            return {
                "name": file.readline().strip(),
                "age": int(file.readline().strip()),
                "hobbies": file.readline().strip().split(","),
            }
