from restful_lib import Connection

from disambiguation_result import DisambiguationResult

# 
# base_url = "http://172.31.1.235:8080"
# 
# conn = Connection(base_url)
# result = conn.request_post("/disambiguate", args={}, body="cat vet", headers={'Accept':'text/json'})
# 
# json.loads(result["body"])

class MeaningRecognitionAPI(object):
	
	def __init__(self, url):
		self.url = url
		self.connection = Connection(self.url)
    
	def recognize(self, text_to_recognize):
		result = self.connection.request_post("/disambiguate", args={}, body=text_to_recognize, headers={'Accept':'text/json'})
		return DisambiguationResult(result["body"])