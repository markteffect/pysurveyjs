from pysurveyjs.values import MissingValue, Value
from pysurveyjs.variables.variable import Variable
from pysurveyjs.values import StringValue


class ImageVariable(Variable):
    image_url: str

    def __init__(self, name: str, image_url: str) -> None:
        self.image_url = image_url

    def get_value(self) -> Value | MissingValue:
        return StringValue(self.image_url)
