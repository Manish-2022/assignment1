import os

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv("dev.env")

CONTAINER_NAME = os.getenv("CONTAINER_NAME")

app = Flask(__name__)


@app.route("/get-data", methods=["GET"])
def get_data():
    prefix = request.args.get("prefix")
    connection_string = os.getenv("CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blobs = container_client.list_blob_names(name_starts_with=prefix)
    # List blobs
    response = []
    for blob in blobs:
        response.append(blob.replace(f"{prefix}/", ""))
    if len(response) == 0:
        return (
            jsonify(
                {
                    "error": f"Either there is no folder named {prefix} or there are no files inside the folder"
                }
            ),
            400,
        )
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
