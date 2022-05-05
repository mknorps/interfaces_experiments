from typing import List

from interfaces.types import Person


class InformalPeopleParserInterface:
    def load_data_source(self, file_path: str) -> str:
        raise NotImplementedError

    def extract_persons(self, file_path: str) -> List[Person]:
        raise NotImplementedError


def mock_data_source(file_path: str) -> str:
    mock = "Lorem impsum: Jonathan 23"
    return mock


class XMLPeopleParserInformal(InformalPeopleParserInterface):
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_persons(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]


class JsonPeopleParserInformal(InformalPeopleParserInterface):
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_persons(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]


class FaultyJsonPeopleParserInformal(InformalPeopleParserInterface):
    def load_data_source(self, file_path: str) -> str:
        return mock_data_source(file_path=file_path)

    def extract_cats(self, file_path: str) -> List[Person]:
        data = self.load_data_source(file_path)
        split_data = data.split(" ")
        return [Person(name=split_data[-2], age=split_data[-1])]