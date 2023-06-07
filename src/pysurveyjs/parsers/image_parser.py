from collections.abc import Iterable
from pysurveyjs.variables.variable import Variable
from pysurveyjs.variables.image_variable import ImageVariable
from pysurveyjs.parser_helpers import *
from pysurveyjs.parsers.base_parser import Parser

class ImageParser(Parser):
  def parse(self, root_parser: Parser, question: dict, data_prefix: list = ...) -> Iterable[Variable]:
    name = extract_valuename(question)
    
    image_url = question.get('imageLink', "")
    
    yield ImageVariable(name, image_url)