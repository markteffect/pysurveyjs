import pytest
from pysurveyjs.parser_helpers import *


def test_extract_valuename() -> None:
    question = {
        "valueName": "test",
        "type": "text",
    }

    valuename = extract_valuename(question)
    assert valuename == "test"

    question = {
        "name": "test2",
        "type": "text",
    }

    valuename = extract_valuename(question)
    assert valuename == "test2"

    question = {"type": "text", "title": {"default": "test"}}

    with pytest.raises(ValueError):
        valuename = extract_valuename(question)


def test_extract_name() -> None:
    question = {
        "name": "test2",
        "type": "text",
    }

    name = extract_name(question)
    assert name == "test2"

    question = {"type": "text", "title": {"default": "test"}}

    with pytest.raises(ValueError):
        name = extract_name(question)


def test_extract_localized_text_simple() -> None:
    question = {
        "name": "V001",
        "type": "radiobutton",
        "title": {
            "default": "Question 1",
            "nl": "Vraag 1",
            "fr": "Question un",
        },
    }

    titles = extract_localized_text(question, "title")

    assert titles["default"] == "Question 1"
    assert titles["nl"] == "Vraag 1"
    assert titles["fr"] == "Question un"


def test_extract_localized_text_defaults() -> None:
    question = {
        "name": "V001",
        "type": "radiobutton",
    }

    titles = extract_localized_text(question, "title", {"default": "Question 1"})

    assert titles["default"] == "Question 1"


def test_extract_localized_text_as_string() -> None:
    question = {"name": "V001", "type": "radiobutton", "title": "test"}

    titles = extract_localized_text(question, "title", {"default": "Question 1"})

    assert titles["default"] == "test"


def test_extract_localized_text_add_defaults() -> None:
    question = {
        "name": "V001",
        "type": "radiobutton",
        "title": {
            "nl": "nl_test",
            "fr": "fr_test",
        },
    }

    titles = extract_localized_text(question, "title", {"default": "test"})

    assert titles["default"] == "test"
    assert titles["nl"] == "nl_test"
    assert titles["fr"] == "fr_test"


def test_extract_choices_simple_string_list() -> None:
    question = {
        "name": "V001",
        "type": "radiobutton",
        "choices": ["Yes", "No", "Maybe"],
    }

    choices = extract_choices(question.get("choices"))
    assert len(choices) == 3

    for choice in choices:
        assert isinstance(choice, StringValueOption)

    assert choices[0].get_raw_value() == choices[0].get_display_value() == "Yes"
    assert choices[1].get_raw_value() == choices[1].get_display_value() == "No"
    assert choices[2].get_raw_value() == choices[2].get_display_value() == "Maybe"


def test_extract_choices_simple_int_list() -> None:
    question = {"name": "V001", "type": "radiobutton", "choices": ["1", "2", "3"]}

    choices = extract_choices(question.get("choices"))
    assert len(choices) == 3

    for choice in choices:
        assert isinstance(choice, IntegerValueOption)

    assert choices[0].get_raw_value() == 1
    assert choices[1].get_raw_value() == 2
    assert choices[2].get_raw_value() == 3

    assert choices[0].get_display_value() == "1"
    assert choices[1].get_display_value() == "2"
    assert choices[2].get_display_value() == "3"


def test_extract_choices_with_key_value() -> None:
    question = {
        "name": "V001",
        "type": "radiobutton",
        "choices": [
            {
                "value": "yes",
                "text": {
                    "default": "Yes",
                    "nl": "Ja",
                },
            },
            {
                "value": "no",
                "text": {
                    "default": "No",
                    "nl": "Nee",
                },
            },
        ],
    }

    choices = extract_choices(question.get("choices"))
    assert len(choices) == 2

    for choice in choices:
        assert isinstance(choice, StringValueOption)

    assert choices[0].get_raw_value() == "yes"
    assert choices[0].get_display_value() == "Yes"
    assert choices[0].get_display_value("nl") == "Ja"

    assert choices[1].get_raw_value() == "no"
    assert choices[1].get_display_value() == "No"
    assert choices[1].get_display_value("nl") == "Nee"
