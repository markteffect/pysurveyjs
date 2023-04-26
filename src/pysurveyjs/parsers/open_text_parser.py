from typing import Iterable
from pysurveyjs.parsers.base_parser import Parser
from pysurveyjs.parser_helpers import *
from pysurveyjs.variables import *


class OpenTextParser(Parser):
    def parse(
        self, root_parser: Parser, question: dict, data_prefix: list = []
    ) -> Iterable[Variable]:
        datapath = [*data_prefix, extract_valuename(question)]

        name = extract_name(question)
        titles = extract_localized_text(question, "title", {"default": name})

        if question.get("inputType") == "number":
            yield NumericVariable(name, titles, datapath)
        else:
            yield StringVariable(name, titles, datapath)
