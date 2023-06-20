from pydantic import BaseModel


class CloudFunctionModel(BaseModel):
    id: str
    content: dict
