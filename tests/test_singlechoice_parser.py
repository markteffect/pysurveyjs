from pysurveyjs.parsers.dummy_parser import DummyParser
from pysurveyjs.parsers.single_choice_parser import SingleChoiceParser
from pysurveyjs.values.integer_value_option import IntegerValueOption
from pysurveyjs.values.invalid_value import InvalidValue
from pysurveyjs.values.string_value_option import StringValueOption
from pysurveyjs.variables.single_choice_variable import SingleChoiceVariable


def test_parse_simple():
    question = {
        'type': 'radiogroup',
        'name': 'question1',
        'choices': [
            '1',
            '2',
            '3',
            '4',
        ],
    }

    root_parser = DummyParser()

    parser = SingleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, SingleChoiceVariable)

    response = {'question1': '3'}

    value = result.get_value(response)

    assert isinstance(value, IntegerValueOption)
    assert value.get_raw_value() == 3
    assert value.get_display_value() == '3'


def test_parse_simple_text():
    question = {
        'type': 'radiogroup',
        'name': 'question1',
        'choices': [
            'one',
            'two',
            'three',
            'four',
        ],
    }

    root_parser = DummyParser()

    parser = SingleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, SingleChoiceVariable)

    response = {'question1': 'two'}

    value = result.get_value(response)

    assert isinstance(value, StringValueOption)
    assert value.get_raw_value() == 'two'
    assert value.get_display_value() == 'two'


def test_parse_key_value():
    question = {
        'type': 'radiogroup',
        'name': 'question1',
        "choices": [
            {
                "value": "one",
                "text": "first",
            },
            {
                "value": "two",
                "text": "second",
            },
            {
                "value": "three",
                "text": "third",
            },
        ],
    }

    root_parser = DummyParser()

    parser = SingleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, SingleChoiceVariable)

    response = {'question1': 'two'}

    value = result.get_value(response)

    assert isinstance(value, StringValueOption)
    assert value.get_raw_value() == 'two'
    assert value.get_display_value() == 'second'


def test_parse_key_value():
    question = {
        'type': 'radiogroup',
        'name': 'question1',
        "choices": [
            {
                "value": "one",
                "text": "first",
            },
            {
                "value": "two",
                "text": "second",
            },
            {
                "value": "three",
                "text": "third",
            },
        ],
    }

    root_parser = DummyParser()

    parser = SingleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, SingleChoiceVariable)

    response = {'question1': 'something_wrong'}

    value = result.get_value(response)

    assert isinstance(value, InvalidValue)


def test_parse_key_value():
    question = {
        'type': 'radiogroup',
        'name': 'question1',
        "choices": [
            {
                "value": "one",
                "text": {
                    'default': 'first',
                    'nl': 'eerste',
                },
            },
            {
                "value": "two",
                "text": {
                    'default': 'second',
                    'nl': 'tweede',
                },
            },
            {
                "value": "three",
                "text": {
                    'default': 'third',
                    'nl': 'derde',
                },
            },
        ],
    }

    root_parser = DummyParser()

    parser = SingleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, SingleChoiceVariable)

    response = {'question1': 'two'}

    value = result.get_value(response)

    assert isinstance(value, StringValueOption)
    assert value.get_raw_value() == 'two'
    assert value.get_display_value() == 'second'
    assert value.get_display_value('nl') == 'tweede'
    
def test_parse_title():
    question = {
        'type': 'radiogroup',
        'name': 'question1',
        'title': {
          'default': 'Question 1',
          'nl': 'Vraag 1',
        },
        "choices": [
            {
                "value": "one",
                "text": {
                    'default': 'first',
                    'nl': 'eerste',
                },
            },
            {
                "value": "two",
                "text": {
                    'default': 'second',
                    'nl': 'tweede',
                },
            },
            {
                "value": "three",
                "text": {
                    'default': 'third',
                    'nl': 'derde',
                },
            },
        ],
    }

    root_parser = DummyParser()

    parser = SingleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, SingleChoiceVariable)
    assert result.get_name() == 'question1'
    assert result.get_title() == 'Question 1'
    assert result.get_title('nl') == 'Vraag 1'

    response = {'question1': 'two'}

    value = result.get_value(response)

    assert isinstance(value, StringValueOption)
    assert value.get_raw_value() == 'two'
    assert value.get_display_value() == 'second'
    assert value.get_display_value('nl') == 'tweede'