from collections.abc import Iterable
from pysurveyjs.parsers.base_parser import Parser
from pysurveyjs.variables.variable import Variable
from pysurveyjs.variables.boolean_variable import BooleanVariable
from pysurveyjs.parser_helpers import *

class BooleanParser(Parser):
  def parse(self, root_parser: Parser, question: dict, data_prefix: list = []) -> Iterable[Variable]:
    datapath = [*data_prefix, extract_valuename(question)]
    
    name = extract_name(question)
    titles = extract_localized_text(question, 'title', {'default': name})
    
    yield BooleanVariable(name, titles, datapath)