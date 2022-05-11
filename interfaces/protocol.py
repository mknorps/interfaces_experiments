from typing import Protocol, List

from interfaces.common import mock_data_source
from interfaces.types import Person


class ProtocolPeopleParserInterface(Protocol):

    def load_data_source(self, file_path: str) -> str:
        ...

    def extract_persons(self, file_path: str) -> List[Person]:
        ...


class XMLPeopleParserProtocol:
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_persons(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]


class JsonPeopleParserProtocol:
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_persons(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]


class FaultyJsonPeopleParserProtocol:
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_cats(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]