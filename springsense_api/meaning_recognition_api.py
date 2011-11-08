from restful_lib import Connection
from urllib import quote

from disambiguation_result import DisambiguationResult

# 
# base_url = "http://172.31.1.235:8080"
# 
# conn = Connection(base_url)
# result = conn.request_post("/disambiguate", args={}, body="cat vet", headers={'Accept':'text/json'})
# 
# json.loads(result["body"])

class MeaningRecognitionAPI(object):
	
	def __init__(self, url, quote=True):
		self.url = url
		self.connection = Connection(self.url)
		self.quote = quote
    
	def recognize(self, text_to_recognize):
		text = text_to_recognize
		if (self.quote):
			text = quote(text)
		result = self.connection.request_post("/disambiguate", args={}, body=text, headers={'Accept':'text/json'})
		return DisambiguationResult(result["body"])