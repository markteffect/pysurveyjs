from value_option import ValueOption


class IntegerValueOption(ValueOption):
    def __init__(self, raw_value: int, display_values: dict[str, str]) -> None:
        super().__init__(raw_value, display_values)

    def get_raw_value(self) -> int:
        return super().get_raw_value()
