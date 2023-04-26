from pysurveyjs.values.value import Value


class MissingValue(Value):
    def __init__(self) -> None:
        self.raw_value = None

    def get_raw_value(self) -> None:
        return None

    def get_display_value(self) -> str:
        return ""
