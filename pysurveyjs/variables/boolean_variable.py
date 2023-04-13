from pysurveyjs.variables.variable import Variable
from pysurveyjs.values import BooleanValue, MissingValue


class BooleanVariable(Variable):
    def get_value(self, record: dict) -> BooleanValue | MissingValue:
        value = super().get_value(record)

        if not isinstance(value, bool):
            return ValueError(f"{self.name}: Value is not Boolean({value})")

        if value is None:
            return MissingValue()

        return BooleanValue(value)
