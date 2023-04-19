from value_option import ValueOption


class StringValueOption(ValueOption):
    def __init__(self, raw_value: str, display_values: dict[str, str]) -> None:
        super().__init__(raw_value, display_values)

    def get_raw_value(self) -> str:
        return super().get_raw_value()
