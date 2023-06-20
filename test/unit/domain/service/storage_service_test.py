import unittest

from faker import Faker

from src.domain.model.cloud_function_model import CloudFunctionModel
from src.domain.port_out.storage_port import StoragePort
from src.domain.service.storage_service import StorageService


class StorageServiceTest(unittest.TestCase):
    __faker: Faker = Faker()

    def test_should_save_model(self):
        # Given
        storage_port_mock = StoragePortMock()
        storage_service = StorageService(storage_port_mock)
        fake_id: str = self.__faker.name()
        fake_content: dict = {
            "title": self.__faker.name(),
            "description": self.__faker.name(),
        }
        model: CloudFunctionModel = CloudFunctionModel(id=fake_id, content=fake_content)

        # When
        storage_service.save(model)

        # Then
        self.assertEqual(storage_port_mock.counter, 1)


class StoragePortMock(StoragePort):
    counter: int

    def __init__(self):
        self.counter = 0

    def save(self, model: CloudFunctionModel):
        self.counter += 1
