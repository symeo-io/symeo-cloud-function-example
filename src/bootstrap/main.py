import flask

from src.application.cloud_function_adapter.adapter.cloud_function_adapter import (
    CloudFunctionAdapter,
)
from src.domain.service.storage_service import StorageService
from src.infrastructure.firestore_storage_adapter.adapter.firestore_storage_adapter import (
    FirestoreStorageAdapter,
)


def cloud_function(request: flask.Request) -> flask.Response:
    key_filename = "key_filename"
    firestore_storage_adapter: FirestoreStorageAdapter = FirestoreStorageAdapter(key_filename)
    storage_service: StorageService = StorageService(firestore_storage_adapter)
    cloud_function_adapter: CloudFunctionAdapter = CloudFunctionAdapter(storage_service)
    return cloud_function_adapter.process(request)


app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    return cloud_function(flask.request)


if __name__ == "__main__":
    # Local dev only
    app.run(host="localhost", port=8000, debug=True)
