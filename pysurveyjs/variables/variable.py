from values import Value, MissingValue


class Variable:
    name = ''
    titles = {}
    data_path = []

    def __init__(self, name: str, titles: dict[str, str], data_path: list[str]) -> None:
        self.name = name
        self.titles = titles
        if not 'default' in self.titles:
            self.titles['default'] = name
        self.data_path = data_path

    def get_title(self, locale: str = 'default') -> str:
        return self.titles.get(locale, self.titles.get('default'))

    def get_name(self) -> str:
        return self.name

    def get_value(self, record: dict) -> str | float | bool | list | None:
        data = record
        # Traverse the entire data path in the data
        for element in self.data_path:
            data = data.get(element)
            if data is None:
                break
        return data
