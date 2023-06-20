from src.domain.model.cloud_function_model import CloudFunctionModel
from src.domain.port_in.storage_facade import StorageFacade
from src.domain.port_out.storage_port import StoragePort


class StorageService(StorageFacade):
    __storage_port: StoragePort

    def __init__(self, storage_port: StoragePort):
        self.__storage_port = storage_port

    def save(self, model: CloudFunctionModel):
        return self.__storage_port.save(model)
