from typing import List, Callable, Optional, Protocol, runtime_checkable

from pydantic import BaseModel

from interfaces.types import Person

@runtime_checkable
class LoadDataSource(Protocol):
    def __call__(self, file_path: str) -> str: ...

@runtime_checkable
class ExtractPersons(Protocol):
    def __call__(self, data: str) -> List[Person]: ...


class FunctionalPeopleParser(BaseModel):
    load_data_source: LoadDataSource
    extract_persons: ExtractPersons

    def get_persons(self, file_path: str) -> List[Person]:
        data: str = self.load_data_source(file_path)
        persons = self.extract_persons(data)
        return persons


def load_xml(file_path: str) -> str:
    mock = "Lorem impsum: Jonathan 23"
    return mock


def load_json(file_path: str) -> str:
    mock = "Lorem impsum: Jonathan 23"
    return mock


def extract_persons_from_xml(data: str) -> List[Person]:
    split_data = data.split(" ")
    return [Person(name=split_data[-2], age=split_data[-1])]


def extract_persons_from_json(data: str) -> List[Person]:
    pass


def extract_persons_from_json_to_dict(data: dict) -> int:
    pass


xml_people_parser = FunctionalPeopleParser(
    load_data_source=load_xml,
    extract_persons= extract_persons_from_xml)

json_people_parser = FunctionalPeopleParser(
    load_data_source=load_json,
    extract_persons= extract_persons_from_json)

faulty_json_people_parser = FunctionalPeopleParser(
    load_data_source=load_json,
    extract_cats= extract_persons_from_json)

faulty_json_people_parser_wrong_type = FunctionalPeopleParser(
    load_data_source=load_json,
    extract_persons= extract_persons_from_json_to_dict)