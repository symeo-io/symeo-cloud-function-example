from src.application.cloud_function_adapter.dto.clound_function_dto import (
    CloudFunctionDTO,
)
from src.domain.model.cloud_function_model import CloudFunctionModel


class CloudFunctionMapper:
    @staticmethod
    def from_request_to_domain(
        cloud_function_dto: CloudFunctionDTO,
    ) -> CloudFunctionModel:
        return CloudFunctionModel(id=cloud_function_dto.id, content=cloud_function_dto.content)
