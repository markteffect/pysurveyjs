from pysurveyjs.variables import Variable
from pysurveyjs.values import NumericValue, MissingValue


class NumericVariable(Variable):
    def get_value(self, record: dict) -> NumericValue | MissingValue:
        value = super().get_value(record)

        if value is None:
            return MissingValue()

        return NumericValue(float(value))
