from pysurveyjs.values.value import Value

class NumericValue(Value):
  
  def __init__(self, raw_value: float) -> None:
    if not isinstance(raw_value, float):
      raw_value = float(raw_value) # Throws an error when it cannot be parsed
    super().__init__(raw_value)
    
  def get_raw_value(self) -> float:
    return super().get_raw_value()