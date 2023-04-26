from pysurveyjs.values.value import Value
class ValueOption(Value):
    DEFAULT_LOCALE = "default"

    raw_value: str | int | float | bool | list | None
    display_values: dict[str, str] = {}

    def __init__(
        self,
        raw_value: str | int | float | bool | list | None,
        display_values: dict[str, str],
    ) -> None:
        self.raw_value = raw_value
        self.display_values = display_values

    def get_display_value(self, locale: str = "default") -> str:
        return self.display_values.get(
            locale, self.display_values.get(self.DEFAULT_LOCALE, str(self.raw_value))
        )

    def get_raw_value(self) -> str | int | float | bool | list | None:
        return self.raw_value
