from pysurveyjs.values import MissingValue, Value
from pysurveyjs.variables.variable import Variable
from pysurveyjs.values import StringValue


class TextVariable(Variable):
    text: str

    def __init__(self, name: str, text: str) -> None:
        self.text = text

    def get_value(self) -> Value | MissingValue:
        return StringValue(self.text)
