from pysurveyjs.values.value import Value

class InvalidValue(Value):
  def __init__(self, raw_value: any = 'Invalid') -> None:
    super().__init__(raw_value)