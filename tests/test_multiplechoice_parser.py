from pysurveyjs.parsers.dummy_parser import DummyParser
from pysurveyjs.parsers.multiple_choice_parser import MultipleChoiceParser
from pysurveyjs.values.integer_value_option import IntegerValueOption
from pysurveyjs.values.invalid_value import InvalidValue
from pysurveyjs.values.string_value_option import StringValueOption
from pysurveyjs.variables.multiple_choice_variable import MultipleChoiceVariable

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

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)

    response = {'question1': ['3']}

    value = result.get_value(response)
    
    assert len(value) == 1

    assert isinstance(value[0], IntegerValueOption)
    assert value[0].get_raw_value() == 3
    assert value[0].get_display_value() == '3'


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

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)

    response = {'question1': ['two']}

    value = result.get_value(response)[0]

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

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)

    response = {'question1': ['two']}

    value = result.get_value(response)[0]

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

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)

    response = {'question1': ['something_wrong']}

    value = result.get_value(response)[0]

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

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)

    response = {'question1': ['two']}

    value = result.get_value(response)[0]

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

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)
    assert result.get_name() == 'question1'
    assert result.get_title() == 'Question 1'
    assert result.get_title('nl') == 'Vraag 1'

    response = {'question1': ['two']}

    value = result.get_value(response)[0]

    assert isinstance(value, StringValueOption)
    assert value.get_raw_value() == 'two'
    assert value.get_display_value() == 'second'
    assert value.get_display_value('nl') == 'tweede'
    
def test_parse_multiple_answers():
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

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)
    assert result.get_name() == 'question1'
    assert result.get_title() == 'Question 1'
    assert result.get_title('nl') == 'Vraag 1'

    response = {'question1': ['two', 'three']}

    values = result.get_value(response)
    
    assert len(values) == 2

    assert isinstance(values[0], StringValueOption)
    assert values[0].get_raw_value() == 'two'
    assert values[0].get_display_value() == 'second'
    assert values[0].get_display_value('nl') == 'tweede'
    
    assert isinstance(values[1], StringValueOption)
    assert values[1].get_raw_value() == 'three'
    assert values[1].get_display_value() == 'third'
    assert values[1].get_display_value('nl') == 'derde'
    
def test_parse_multiple_answers_mixed_type():
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
            '4',
        ],
    }

    root_parser = DummyParser()

    parser = MultipleChoiceParser()

    result = parser.parse(root_parser, question)

    assert isinstance(result, MultipleChoiceVariable)
    assert result.get_name() == 'question1'
    assert result.get_title() == 'Question 1'
    assert result.get_title('nl') == 'Vraag 1'

    response = {'question1': ['two', '4']}

    values = result.get_value(response)
    
    assert len(values) == 2

    assert isinstance(values[0], StringValueOption)
    assert values[0].get_raw_value() == 'two'
    assert values[0].get_display_value() == 'second'
    assert values[0].get_display_value('nl') == 'tweede'
    
    assert isinstance(values[1], IntegerValueOption)
    assert values[1].get_raw_value() == 4
    assert values[1].get_display_value() == '4'
    assert values[1].get_display_value('nl') == '4'