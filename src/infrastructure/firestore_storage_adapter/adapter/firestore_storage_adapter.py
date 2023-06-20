from google.auth.credentials import Credentials
from google.cloud import datastore
from google.cloud.datastore import Client, Entity, Key
from google.oauth2 import service_account


from src.domain.model.cloud_function_model import CloudFunctionModel
from src.domain.port_out.storage_port import StoragePort


class FirestoreStorageAdapter(StoragePort):
    __firestore_client: Client

    def __init__(self, key_filename):
        credentials: Credentials = service_account.Credentials.from_service_account_file(key_filename)
        self.__firestore_client = datastore.Client(credentials=credentials)

    def save(self, model: CloudFunctionModel):
        datastore_key: Key = self.__firestore_client.key("Model", model.id)
        model_entity: Entity = datastore.Entity(key=datastore_key)
        model_entity.update(model.content)
        self.__firestore_client.put(model_entity)
        return datastore_key.path
