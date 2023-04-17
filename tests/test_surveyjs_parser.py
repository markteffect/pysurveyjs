from pysurveyjs import SurveyJSParser
def test_parse_happy_flow():
  survey = {
    'pages': [
      {
        'elements': [
          {
            'type': 'text',
            'name': 'question1',
          },
        ],
      },
    ],
  }
  
  parser = SurveyJSParser()
  
  result = parser.parse_survey(survey)
  
  assert len(list(result)) == 1
  