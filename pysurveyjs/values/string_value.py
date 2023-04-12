from value import Value

class StringValue(Value):
  
  def __init__(self, raw_value: str) -> None:
    if not isinstance(raw_value, str):
      raise ValueError(f"{raw_value} is not a string")
    super().__init__(raw_value)
  
  def get_raw_value(self) -> str:
    return super().get_raw_value()
    