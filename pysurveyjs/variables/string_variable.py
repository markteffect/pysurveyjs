from pysurveyjs.variables.variable import Variable
from pysurveyjs.values import StringValue, MissingValue

class StringVariable(Variable):
    def get_value(self, record: dict) -> StringValue | MissingValue:
        value = super().get_value(record)
        
        if value is None:
          return MissingValue()
        
        return StringValue(str(value))