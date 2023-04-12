def extract_valuename(element: dict) -> str:
  valuename = element.get('valueName', element.get('name'))
  if valuename is None or not isinstance(valuename, str):
    raise ValueError(f'valueName or name must exist and be string, found: {valuename}')
  
def extract_name(element: dict) -> str:
  name = element.get('name')
  if name is None or not isinstance(name, str):
    raise ValueError(f'name must exist and be string, found: {name}')
  
def extract_localized_text(element: dict, field: str = 'text', defaults: dict[str, str] = {}) -> dict[str, str]:
  if element.get(field) is None:
    return defaults
  
  value = element.get(field)
  
  if isinstance(value, str):
    return {
      'default': value,
    }
  elif isinstance(value, dict):
    result = defaults # Merge defaults and value
    for locale, value in value.items(): 
      result[locale] = value
    return result
  else:
    raise ValueError(f"Expected string or dict for field {field}, found {value}")

