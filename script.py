import os

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv("dev.env")

CONTAINER_NAME = os.getenv("CONTAINER_NAME")

connection_string = os.getenv("CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# List blobs
for blob in container_client.list_blobs():
    print(blob.name)
