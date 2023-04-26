from pysurveyjs.values import MissingValue, Value
from pysurveyjs.variables.variable import Variable
from pysurveyjs.values.value_option import ValueOption
from pysurveyjs.values.invalid_value import InvalidValue

class SingleChoiceVariable(Variable):
  
  valuemap: dict[str, ValueOption] = []
  
  def __init__(self, name: str, titles: dict[str, str], data_path: list[str], value_options: list[ValueOption]) -> None:
    super().__init__(name, titles, data_path)
    
    for option in value_options:
      self.valuemap[str(option.get_raw_value())] = option
      
  def get_value(self, record: dict) -> Value | MissingValue:
    raw_value = super().get_value(record)
    
    if raw_value in self.valuemap.keys() and self.valuemap[raw_value] != None:
      return self.valuemap[raw_value]
    
    return InvalidValue()