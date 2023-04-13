from pysurveyjs.parser_helpers import *

import pprint
import sys
pprint.pprint(sys.path)

def test_extract_valuename():
  question = {
    'valueName': 'test',
    'type': 'text',
  }
  
  valuename = extract_valuename(question)
  assert valuename == 'test'