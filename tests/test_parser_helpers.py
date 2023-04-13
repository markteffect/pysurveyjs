import pytest
from pysurveyjs.parser_helpers import *


def test_extract_valuename():
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


def test_extract_name():
    question = {
        "name": "test2",
        "type": "text",
    }

    name = extract_name(question)
    assert name == "test2"

    question = {"type": "text", "title": {"default": "test"}}

    with pytest.raises(ValueError):
        name = extract_name(question)


def test_extract_localized_text_simple():
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


def test_extract_localized_text_defaults():
    question = {
        "name": "V001",
        "type": "radiobutton",
    }

    titles = extract_localized_text(question, "title", {"default": "Question 1"})

    assert titles["default"] == "Question 1"


def test_extract_localized_text_as_string():
    question = {"name": "V001", "type": "radiobutton", "title": "test"}

    titles = extract_localized_text(question, "title", {"default": "Question 1"})

    assert titles["default"] == "test"


def test_extract_localized_text_add_defaults():
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
