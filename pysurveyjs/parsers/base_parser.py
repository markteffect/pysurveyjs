from collections.abc import Iterable
from variables import Variable
from pysurveyjs.parsers.base_parser import Parser

class Parser:
  def parse(root_parser: Parser, question: dict, data_prefix: list) -> Iterable[Variable]:
    raise NotImplementedError('Every parser should implement their own parse() method')