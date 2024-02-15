from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ServerASerializer
from pathlib import Path
import json
import yaml
import os
import requests


# Base directory for data files
DATA_FILES_DIR = Path(__file__).resolve().parent.parent / "data_files"


class BaseDataViewSet(viewsets.ViewSet):
    """
    A base viewset for reading and parsing data from files.
    """

    def list(self, request):
        # Placeholder for parsing logic specific to each file format
        parsed_data = self.parse_data()

        # Serializing the parsed data
        serializer = ServerASerializer(data=parsed_data)
        serializer.is_valid(raise_exception=True)  # Validate the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def parse_data(self):
        # Placeholder method to be overridden in subclass viewsets
        raise NotImplementedError("Subclasses must implement parse_data method")


class JsonDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.json"
        with open(file_path, "r") as file:
            return json.load(file)


class YamlDataViewSet(BaseDataViewSet):
    def parse_data(self):
        file_path = DATA_FILES_DIR / "anna.yml"
        with open(file_path, "r") as file:
            return yaml.safe_load(file)


class ReadCSVFromServerBViewSet(viewsets.ViewSet):
    def list(self, request):
        response = requests.get("http://localhost:8080/parser/csv/")
        response.raise_for_status()
        return Response(response.json(), status=status.HTTP_200_OK)


class ReadXMLFromServerBViewSet(viewsets.ViewSet):
    def list(self, request):
        response = requests.get("http://localhost:8080/parser/xml/")
        response.raise_for_status()
        return Response(response.json(), status=status.HTTP_200_OK)
