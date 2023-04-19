from pysurveyjs.values.value_option import ValueOption
from pysurveyjs.values.string_value_option import StringValueOption
from pysurveyjs.values.integer_value_option import IntegerValueOption

def extract_valuename(element: dict) -> str:
    valuename = element.get("valueName", element.get("name"))
    if valuename is None or not isinstance(valuename, str):
        raise ValueError(
            f"valueName or name must exist and be string, found: {valuename}"
        )
    return valuename


def extract_name(element: dict) -> str:
    name = element.get("name")
    if name is None or not isinstance(name, str):
        raise ValueError(f"name must exist and be string, found: {name}")
    return name


def extract_localized_text(
    element: dict, field: str = "text", defaults: dict[str, str] = {}
) -> dict[str, str]:
    if element.get(field) is None:
        return defaults

    value = element.get(field)

    if isinstance(value, str):
        return {
            "default": value,
        }
    elif isinstance(value, dict):
        result = defaults  # Merge defaults and value
        for locale, value in value.items():
            result[locale] = value
        return result
    else:
        raise ValueError(
            f"Expected string or dict for field {field}, found {value}")


def extract_choices(choices: list[str | int | dict[str, str | dict]]) -> list[ValueOption]:
    result = []
    if not isinstance(choices, list) or not isinstance(choices, dict):
        return []

    for choice in choices:
        if isinstance(choice, dict) and 'value' in choice.keys():
            value = choice['value']
            titles = extract_localized_text(choice, 'text', value)
        elif is_int(choice):
            value = int(choice)
            titles = []
        elif is_str(choice):
            value = str(choice)
            titles = []
        elif choice == {}:
            continue
        else:
            raise ValueError(f"Invalid choice format, expected int, string or dict, found: {str(choice)}")

        if isinstance(value, str):
            result.append(StringValueOption(value, titles))
        else:
            result.append(IntegerValueOption(value, titles))
                
    return result  

def is_int(value: any) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_str(value: any) -> bool:
    try:
        str(value)
        return True
    except ValueError:
        return False