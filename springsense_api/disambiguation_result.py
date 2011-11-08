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

	def variants(self):
		sentences = self.sentences()
		
		list_of_variant_sentence_lists = map(lambda sentence: sentence.variants(), sentences)
		max_length_of_variant_sentences = max([len(variant_sentences) for variant_sentences in list_of_variant_sentence_lists])
		
		padded_list_of_variant_sentence_lists = []
		for variant_sentences in list_of_variant_sentence_lists:
			while len(variant_sentences) < max_length_of_variant_sentences: 
				variant_sentences.append(variant_sentences[0])
			padded_list_of_variant_sentence_lists.append(variant_sentences) 
		
		transposed = map(lambda *row: list(row), *padded_list_of_variant_sentence_lists)
	
		variants = []
		for idx, variant_sentences in enumerate(transposed):
			variants.append(Variant(idx, variant_sentences))
			
		return variants

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
		
	def variants(self):
		variants = []
		scores = self.scores()
		score_count = len(scores)
		cardinality = max(1, score_count)
		for idx in range(cardinality):
			if (idx < score_count):
				score = scores[idx]
			else:
				score = 1.0
			variants.append(VariantSentence(idx, score, []))
			
		for term in self.terms():
			resolved_terms_for_term = self._term_to_resolved_terms(term, cardinality, scores)
			for idx, variant in enumerate(variants):
				variant.resolved_terms.append(resolved_terms_for_term[idx])

		return variants
		
	def _term_to_resolved_terms(self, term, cardinality, scores):
		resolved_terms_for_term = []
		meanings = term.meanings()
		num_meanings = len(meanings)
		if (num_meanings < 1):
			term_with_no_meanings = ResolvedTerm(term, None, 1.0)
			for i in range(cardinality):
				resolved_terms_for_term.append(term_with_no_meanings)
			return resolved_terms_for_term
		
		resolved_terms_by_meaning = {}
		for i in range(cardinality):
			meaning = meanings[i % num_meanings]
			meaning_token = meaning.meaning()
			if meaning_token in resolved_terms_by_meaning:
				# Existing resolved term
				resolved_term = resolved_terms_by_meaning[meaning_token]
				resolved_term.score = resolved_term.score + scores[i]
			else:
				# New resolved term
				resolved_term = ResolvedTerm(term, meaning, scores[i])
				resolved_terms_by_meaning[meaning_token] = resolved_term
		
			resolved_terms_for_term.append(resolved_term)
			
		return resolved_terms_for_term

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
				
	def __repr__(self):
		return self.parsed.__repr__()

	def __str__(self):
		return self.term()

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
		
	def is_entity_type(self):
		return self.meaning() in ["person_n_01", "association_n_01", "location_n_01"]

	def __repr__(self):
		return self.parsed.__repr__()

	def __str__(self):
		return self.meaning()
		
class VariantSentence(object):
	def __init__(self, index, score, resolved_terms):
		self.index = index
		self.score = score
		self.resolved_terms = resolved_terms

	def __str__(self):
		return ' '.join([resolved_term.__str__() for resolved_term in self.resolved_terms])
	
class Variant(object):
	def __init__(self, index, variant_sentences):
		self.index = index
		self.sentences = variant_sentences

	def __str__(self):
		return ' '.join([variant_sentence.__str__() for variant_sentence in self.sentences])
		
class ResolvedTerm(object):
	def __init__(self, term, meaning, score):
		self.term = term
		self.meaning = meaning
		self.score = score

	def __repr__(self):
		return "ResolvedTerm(\tterm= %s,\tmeaning= %s,\tscore= %s)" % (self.term.__str__(), self.meaning.__str__(), self.score.__str__())

	def __str__(self):
		if (self.meaning is None) or (self.meaning.is_entity_type()): 
			return self.term.__str__()
		
		return self.meaning.__str__()	