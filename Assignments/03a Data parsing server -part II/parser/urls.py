from django.urls import path
from .views import (
    JsonDataViewSet,
    YamlDataViewSet,
    ReadCSVFromServerBViewSet,
    ReadXMLFromServerBViewSet,
)

# Define the URL patterns for each data format endpoint
urlpatterns = [
    # path("parser/", include("parser.urls")),
    path("data/json/", JsonDataViewSet.as_view({"get": "list"}), name="json-data"),
    path("data/yaml/", YamlDataViewSet.as_view({"get": "list"}), name="yaml-data"),
    # path for reading data from server B
    path("data/server-b/csv", ReadCSVFromServerBViewSet.as_view({"get": "list"}), name="server-b-csv"),
    path("data/server-b/xml", ReadXMLFromServerBViewSet.as_view({"get": "list"}), name="server-b-xml"),
]
