from typing import Iterable
from pysurveyjs.parsers.base_parser import Parser
from pysurveyjs.parser_helpers import *
from pysurveyjs.variables.variable import Variable
from pysurveyjs.variables.single_choice_variable import SingleChoiceVariable


class SingleChoiceParser(Parser):
    def parse(
        self, root_parser: Parser, question: dict, data_prefix: list = []
    ) -> Iterable[Variable]:
        datapath = [*data_prefix, extract_valuename(question)]

        name = extract_name(question)
        titles = extract_localized_text(question, "title", {"default": name})
        choices = extract_choices(question.get("choices", []))
        
        return SingleChoiceVariable(name, titles, datapath, choices)
