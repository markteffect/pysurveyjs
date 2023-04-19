from pysurveyjs import SurveyJSParser
from pysurveyjs import StringVariable


def test_parse_happy_flow():
    survey = {
        "pages": [
            {
                "elements": [
                    {
                        "type": "text",
                        "name": "question1",
                    },
                ],
            },
        ],
    }

    parser = SurveyJSParser()

    result = list(parser.parse_survey(survey))

    assert len(result) == 1
    assert result[0].get_name() == "question1"
    assert result[0].get_title() == "question1"
    assert isinstance(result[0], StringVariable)


def test_parse_multiple():
    survey = {
        "pages": [
            {
                "elements": [
                    {
                        "type": "text",
                        "name": "question1",
                    },
                    {
                        "type": "text",
                        "name": "question2",
                    },
                ],
            },
        ],
    }

    parser = SurveyJSParser()

    result = list(parser.parse_survey(survey))

    assert len(result) == 2
    assert result[0].get_name() == "question1"
    assert isinstance(result[0], StringVariable)
    assert result[1].get_name() == "question2"
    assert isinstance(result[1], StringVariable)


def test_parse_title():
    survey = {
        "pages": [
            {
                "elements": [
                    {
                        "type": "text",
                        "name": "question1",
                        "title": {
                            "default": "question1",
                            "nl": "vraag1",
                        },
                    },
                ],
            },
        ],
    }

    parser = SurveyJSParser()

    result = list(parser.parse_survey(survey))

    assert len(result) == 1
    assert result[0].get_name() == "question1"
    assert result[0].get_title() == "question1"
    assert result[0].get_title("nl") == "vraag1"
