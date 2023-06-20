import flask

from src.application.cloud_function_adapter.dto.clound_function_dto import (
    CloudFunctionDTO,
)
from src.application.cloud_function_adapter.mapper.cloud_function_mapper import (
    CloudFunctionMapper,
)
from src.domain.port_in.storage_facade import StorageFacade


class CloudFunctionAdapter:
    __storage_facade: StorageFacade

    def __init__(self, storage_facade: StorageFacade):
        self.__storage_facade = storage_facade

    def process(self, request: flask.Request) -> flask.Response:
        request_dto: CloudFunctionDTO = CloudFunctionDTO.parse_obj(request.get_json())
        return self.__storage_facade.save(CloudFunctionMapper.from_request_to_domain(request_dto))
