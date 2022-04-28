from urllib.parse import urlencode, unquote, quote_plus

import requests 

from bs4 import BeautifulSoup

API_KEY = "http://211.237.50.150:7080/openapi/"
serviceKey = 'a1d956a4fe0503826e01e48d39d66db8a1fbd9fa46fb01f0e33b464c64c75b54'


def test_receipe() :    
    TYPE ="json"
    API_URL = 'Grid_000001'
    START_INDEX='1'
    END_INDEX = '100'
    
    