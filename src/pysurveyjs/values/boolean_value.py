from pysurveyjs.values.value import Value


class BooleanValue(Value):
    def __init__(self, raw_value: bool) -> None:
        if not isinstance(raw_value, bool):
            raise ValueError(f"{raw_value} is not a boolean")
        super().__init__(raw_value)

    def get_raw_value(self) -> bool:
        return super().get_raw_value()
