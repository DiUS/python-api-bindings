from restful_lib import Connection
from urllib import quote

from disambiguation_result import DisambiguationResult

class MeaningRecognitionAPI(object):
	
	def __init__(self, url, quote=True):
		self.url = url
		self.connection = Connection(self.url)
		self.quote = quote
    
	def recognize(self, text_to_recognize):
		text = text_to_recognize.encode('utf-8')
		if (self.quote):
			text = quote(text)
		result = self.connection.request_post("/disambiguate", args={}, body=text, headers={'Accept':'text/json'})
		return DisambiguationResult(result["body"])