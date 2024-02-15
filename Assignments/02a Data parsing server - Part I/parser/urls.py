from django.urls import path
from .views import (
    JsonDataViewSet,
    CsvDataViewSet,
    YamlDataViewSet,
    XmlDataViewSet,
    TxtDataViewSet,
)

# Define the URL patterns for each data format endpoint
urlpatterns = [
    path("data/json/", JsonDataViewSet.as_view({"get": "list"}), name="json-data"),
    path("data/csv/", CsvDataViewSet.as_view({"get": "list"}), name="csv-data"),
    path("data/yaml/", YamlDataViewSet.as_view({"get": "list"}), name="yaml-data"),
    path("data/xml/", XmlDataViewSet.as_view({"get": "list"}), name="xml-data"),
    path("data/txt/", TxtDataViewSet.as_view({"get": "list"}), name="txt-data"),
]
