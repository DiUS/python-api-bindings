from restful_lib import Connection
from urllib import quote

from disambiguation_result import DisambiguationResult

class MeaningRecognitionAPI(object):
	
	def __init__(self, url, app_id = None, app_key = None):
		self.url = url
		self.app_id = app_id
		self.app_key = app_key
		self.connection = Connection(self.url)
    
	def recognize(self, text_to_recognize):
		args = { 'body': text_to_recognize.encode('utf-8') }
		if (self.app_id):
			args['app_id'] = self.app_id
		if (self.app_key):
			args['app_key'] = self.app_key
		result = self.connection.request_get('/v1/disambiguate', args= args, headers={'Accept':'text/json'})
		if (result['headers']['status'] != '200'):
			raise IOError('Failed to make disambiguation request', result)
		return DisambiguationResult(result["body"])