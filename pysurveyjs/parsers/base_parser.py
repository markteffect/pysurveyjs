from collections.abc import Iterable
from pysurveyjs.variables.variable import Variable

class Parser:
  def parse(root_parser: 'Parser', question: dict, data_prefix: list) -> Iterable[Variable]:
    raise NotImplementedError('Every parser should implement their own parse() method')