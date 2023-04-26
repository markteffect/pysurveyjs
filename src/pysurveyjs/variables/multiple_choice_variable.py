from pysurveyjs.values import MissingValue, Value
from pysurveyjs.variables.variable import Variable
from pysurveyjs.values.value_option import ValueOption
from pysurveyjs.values.invalid_value import InvalidValue

class MultipleChoiceVariable(Variable):
  
  valuemap: dict[str, ValueOption] = {}
  
  def __init__(self, name: str, titles: dict[str, str], data_path: list[str], value_options: list[ValueOption]) -> None:
    super().__init__(name, titles, data_path)
    
    for option in value_options:
      self.valuemap[str(option.get_raw_value())] = option
  
  def get_value(self, record: dict) -> list[Value] | InvalidValue | MissingValue:
    result = []
    raw_values = super().get_value(record)
    
    for raw_value in raw_values:
      if raw_value in self.valuemap.keys() and self.valuemap[raw_value] != None:
        result.append(self.valuemap[raw_value])
      else:
        result.append(InvalidValue())
    
    return result
  
  def get_value_options(self) -> list[ValueOption]:
    return self.valuemap.values()