from pysurveyjs.variables import Variable
from collections.abc import Iterable
from pysurveyjs.parsers.base_parser import Parser


class SurveyJSParser:
    locale = "en"

    parsers: dict[str, Parser] = {}

    def __init__(self, locale: str = "en") -> None:
        self.locale = locale

    def parse_survey(self, survey: dict) -> Iterable[Variable]:
        pages = survey.get("pages")

        if pages is None or len(pages) is 0:
            raise ValueError("Survey does not contain any pages")

        for page in pages:
            yield from self.parse_page(page)

    def parse_page(self, page: list[dict]) -> Iterable[Variable]:
        for item in page:
            yield from self.parse_element(item)

    def parse_element(self, element: dict) -> Iterable[Variable]:
        question_type = element.get("type")

        if question_type is None:
            raise ValueError(f"Could not find type in element {element}")

        parser = self.parsers.get(question_type)
        if parser is None:
            raise NotImplementedError(
                f"No parser found for question type {question_type}"
            )

        yield from parser.parse(element)
