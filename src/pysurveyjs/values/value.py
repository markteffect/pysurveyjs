class Value:
    raw_value: any

    def __init__(self, raw_value: any) -> None:
        self.raw_value = raw_value

    def get_raw_value(self) -> str | int | float | bool | list | None:
        return self.raw_value

    def get_display_value(self) -> str:
        return str(self.raw_value)
