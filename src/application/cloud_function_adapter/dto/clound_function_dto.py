from pydantic import BaseModel


class CloudFunctionDTO(BaseModel):
    id: str
    content: dict
