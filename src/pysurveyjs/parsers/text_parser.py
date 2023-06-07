from collections.abc import Iterable
from pysurveyjs.variables.variable import Variable
from pysurveyjs.variables.text_variable import TextVariable
from pysurveyjs.parser_helpers import *
from pysurveyjs.parsers.base_parser import Parser

class TextParser(Parser):
  def parse(self, root_parser: Parser, question: dict, data_prefix: list = ...) -> Iterable[Variable]:
    name = extract_valuename(question)
    
    text = question.get('text', "")
    
    yield TextVariable(name, text)