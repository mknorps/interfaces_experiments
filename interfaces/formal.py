import abc
from typing import List

from interfaces.types import Person


class FormalPeopleParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_persons') and
                callable(subclass.extract_persons) or
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, file_path: str):
        raise NotImplementedError

    @abc.abstractmethod
    def extract_persons(self, file_path: str):
        raise NotImplementedError


def mock_data_source(file_path: str) -> str:
    mock = "Lorem impsum: Jonathan 23"
    return mock


class XMLPeopleParserFormal(FormalPeopleParserInterface):
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_persons(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]


class JsonPeopleParserFormal(FormalPeopleParserInterface):
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_persons(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]


class FaultyJsonPeopleParserFormal(FormalPeopleParserInterface):
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_cats(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]