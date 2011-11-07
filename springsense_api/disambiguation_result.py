import simplejson as json

class DisambiguationResult(object):
	
	def __init__(self, json):
		self.json = json
		self.parse()
		
	def parse(self):
		self.parsed = json.loads(self.json)
		
	def sentences(self):
		sentences = []
		for parsed_sentence in self.parsed:
			sentences.append(Sentence(parsed_sentence))
		
		return sentences

class Sentence(object):
	def __init__(self, parsed):
		self.parsed = parsed
		self.parse()	
		
	def parse(self):
		return self.parsed

	def terms(self):
		terms = []
		for parsed_term in self.parsed["terms"]:
			terms.append(Term(parsed_term))
			
		return terms

	def scores(self):
		return self.parsed["scores"]

class Term(object):
	def __init__(self, parsed):
		self.parsed = parsed
		self.parse()	

	def parse(self):
		return self.parsed

	def term(self):
		return self.parsed["term"]

	def word(self):
		return self.parsed["word"]

	def POS(self):
		return self.parsed["POS"]

	def lemma(self):
		return self.parsed["lemma"]

	def offset(self):
		return self.parsed["offset"]

	def meanings(self):
		meanings = []
		for parsed_meaning in self.parsed["meanings"]:
			meanings.append(Meaning(parsed_meaning))	
			
		return meanings

class Meaning(object):
	def __init__(self, parsed):
		self.parsed = parsed
		self.parse()	

	def parse(self):
		return self.parsed

	def definition(self):
		return self.parsed["definition"]
		
	def meaning(self):
		return self.parsed["meaning"]
	