from typing import Iterable
from pysurveyjs.parsers.base_parser import Parser
from pysurveyjs.variables.variable import Variable

class DummyParser(Parser):
  def parse(self, root_parser: Parser, question: dict, data_prefix: list = []) -> Iterable[Variable]:
    return []