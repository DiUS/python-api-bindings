import unittest
from springsense_api.disambiguation_result import DisambiguationResult

class TestDisambiguationResult(unittest.TestCase):
	
	def setUp(self):
		# Lightly grease the pan with butter or cooking spray. Cook large spoonfuls of batter until bubbles burst on the surface and the edges start to go dry.
		self.json = u'[{"terms":[{"term":"Lightly","lemma":"light","word":"Lightly","POS":"RB","offset":0,"meanings":[]},{"term":"grease","lemma":"grease","word":"grease","POS":"NN","offset":8,"meanings":[{"definition":"a thick fatty oil (especially one used to lubricate machinery)","meaning":"grease_n_01"},{"definition":"the state of being covered with unclean things","meaning":"dirt_n_02"},{"definition":"a thick fatty oil (especially one used to lubricate machinery)","meaning":"grease_n_01"}]},{"term":"the","lemma":"the","word":"the","POS":"DT","offset":15,"meanings":[]},{"term":"pan","lemma":"pan","word":"pan","POS":"NN","offset":19,"meanings":[{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"},{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"},{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"}]},{"term":"with","lemma":"with","word":"with","POS":"IN","offset":23,"meanings":[]},{"term":"butter","lemma":"butter","word":"butter","POS":"NN","offset":28,"meanings":[{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"},{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"},{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"}]},{"term":"or","lemma":"or","word":"or","POS":"CC","offset":35,"meanings":[]},{"term":"cooking","lemma":"cooking","word":"cooking","POS":"JJ","offset":38,"meanings":[{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"},{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"},{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"}]},{"term":"spray","lemma":"spray","word":"spray","POS":"NN","offset":46,"meanings":[{"definition":"a jet of vapor","meaning":"spray_n_06"},{"definition":"a jet of vapor","meaning":"spray_n_06"},{"definition":"a pesticide in suspension or solution; intended for spraying","meaning":"spray_n_01"}]},{"term":".","lemma":".","word":".","POS":".","offset":51,"meanings":[]}],"scores":[0.3550889426044858,0.33551600342819754,0.3093950539673166]},{"terms":[{"term":"Cook","lemma":"Cook","word":"Cook","POS":"NNP","offset":53,"meanings":[{"definition":"someone who cooks food","meaning":"cook_n_01"},{"definition":"someone who cooks food","meaning":"cook_n_01"},{"definition":"English navigator who claimed the east coast of Australia for Britain and discovered several Pacific islands (1728-1779)","meaning":"cook_n_02"}]},{"term":"large","lemma":"large","word":"large","POS":"JJ","offset":58,"meanings":[]},{"term":"spoonfuls","lemma":"spoonful","word":"spoonfuls","POS":"NNS","offset":64,"meanings":[{"definition":"as much as a spoon will hold","meaning":"spoon_n_02"},{"definition":"as much as a spoon will hold","meaning":"spoon_n_02"},{"definition":"as much as a spoon will hold","meaning":"spoon_n_02"}]},{"term":"of","lemma":"of","word":"of","POS":"IN","offset":74,"meanings":[]},{"term":"batter","lemma":"batter","word":"batter","POS":"VB","offset":77,"meanings":[{"definition":"(baseball) a ballplayer who is batting","meaning":"batter_n_01"},{"definition":"(baseball) a ballplayer who is batting","meaning":"batter_n_01"},{"definition":"(baseball) a ballplayer who is batting","meaning":"batter_n_01"}]},{"term":"until","lemma":"until","word":"until","POS":"IN","offset":84,"meanings":[]},{"term":"bubbles","lemma":"bubble","word":"bubbles","POS":"NNS","offset":90,"meanings":[{"definition":"a hollow globule of gas (e.g., air or carbon dioxide)","meaning":"bubble_n_01"},{"definition":"a hollow globule of gas (e.g., air or carbon dioxide)","meaning":"bubble_n_01"},{"definition":"a hollow globule of gas (e.g., air or carbon dioxide)","meaning":"bubble_n_01"}]},{"term":"burst","lemma":"burst","word":"burst","POS":"VBN","offset":98,"meanings":[{"definition":"the act of exploding or bursting","meaning":"explosion_n_02"},{"definition":"the act of exploding or bursting","meaning":"explosion_n_02"},{"definition":"the act of exploding or bursting","meaning":"explosion_n_02"}]},{"term":"on","lemma":"on","word":"on","POS":"IN","offset":104,"meanings":[]},{"term":"the","lemma":"the","word":"the","POS":"DT","offset":107,"meanings":[]},{"term":"surface","lemma":"surface","word":"surface","POS":"NN","offset":111,"meanings":[{"definition":"the extended two-dimensional outer boundary of a three-dimensional object","meaning":"surface_n_02"},{"definition":"the outer boundary of an artifact or a material layer constituting or resembling such a boundary","meaning":"surface_n_01"},{"definition":"the extended two-dimensional outer boundary of a three-dimensional object","meaning":"surface_n_02"}]},{"term":"and","lemma":"and","word":"and","POS":"CC","offset":119,"meanings":[]},{"term":"the","lemma":"the","word":"the","POS":"DT","offset":123,"meanings":[]},{"term":"edges","lemma":"edge","word":"edges","POS":"NNS","offset":127,"meanings":[{"definition":"a line determining the limits of an area","meaning":"boundary_n_02"},{"definition":"a line determining the limits of an area","meaning":"boundary_n_02"},{"definition":"a line determining the limits of an area","meaning":"boundary_n_02"}]},{"term":"start","lemma":"start","word":"start","POS":"VB","offset":133,"meanings":[]},{"term":"to","lemma":"to","word":"to","POS":"RP","offset":139,"meanings":[]},{"term":"go","lemma":"go","word":"go","POS":"VB","offset":142,"meanings":[]},{"term":"dry","lemma":"dry","word":"dry","POS":"JJ","offset":145,"meanings":[]},{"term":".","lemma":".","word":".","POS":".","offset":148,"meanings":[]}],"scores":[0.35713964749460503,0.33888255810526546,0.3039777944001295]}]'
		self.result = DisambiguationResult(self.json)
		self.variants = self.result.variants()
		
	def test_should_initialize_correctly(self):
		self.assertEqual(self.json, self.result.json)

	def test_sentences(self):
		self.assertEqual(2, len(self.result.sentences()))

	def test_first_sentence(self):
		first_sentence = self.result.sentences()[0]
		first_sentence_scores = first_sentence.scores()
		self.assertEqual(3, len(first_sentence_scores))
		self.assertEqual(10, len(first_sentence.terms()))

	def test_term_with_meanings(self):
		term_with_meanings = self.result.sentences()[0].terms()[1]
		self.assertEqual("grease", term_with_meanings.term())
		self.assertEqual("grease", term_with_meanings.lemma())
		self.assertEqual("grease", term_with_meanings.word())
		self.assertEqual("NN", term_with_meanings.POS())
		self.assertEqual(8, term_with_meanings.offset())
		self.assertEqual(3, len(term_with_meanings.meanings()))

	def test_term_with_no_meanings(self):
		term_with_meanings = self.result.sentences()[0].terms()[0]
		self.assertEqual("Lightly", term_with_meanings.term())
		self.assertEqual("light", term_with_meanings.lemma())
		self.assertEqual("Lightly", term_with_meanings.word())
		self.assertEqual("RB", term_with_meanings.POS())
		self.assertEqual(0, term_with_meanings.offset())
		self.assertEqual(0, len(term_with_meanings.meanings()))

	def test_meaning(self):
		meaning = self.result.sentences()[0].terms()[1].meanings()[0]
		self.assertEqual("grease_n_01", meaning.meaning())
		self.assertEqual("a thick fatty oil (especially one used to lubricate machinery)", meaning.definition())

	def test_should_have_three_variants(self):
		self.assertEqual(3, len(self.variants))

	def test_variant_transposition(self):
		first_variant = self.variants[0]
		self.assertEquals(first_variant.sentences[0].__str__(), self.result.sentences()[0].variants()[0].__str__())
		self.assertEquals(first_variant.sentences[1].__str__(), self.result.sentences()[1].variants()[0].__str__())
		
		self.assertEquals(u'Lightly grease_n_01 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 . cook_n_01 large spoon_n_02 of batter_n_01 until bubble_n_01 explosion_n_02 on the surface_n_02 and the boundary_n_02 start to go dry .', first_variant.__str__())

		second_variant = self.variants[1]
		self.assertEquals(second_variant.sentences[0].__str__(), self.result.sentences()[0].variants()[1].__str__())
		self.assertEquals(second_variant.sentences[1].__str__(), self.result.sentences()[1].variants()[1].__str__())
		
		self.assertEquals(u'Lightly dirt_n_02 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 . cook_n_01 large spoon_n_02 of batter_n_01 until bubble_n_01 explosion_n_02 on the surface_n_01 and the boundary_n_02 start to go dry .', second_variant.__str__())

		
class TestSentenceVariantsWithMultipleMeanings(unittest.TestCase):

	def setUp(self):
		# "Lightly grease the pan with butter or cooking spray."
		self.json = u'[{"terms":[{"term":"Lightly","lemma":"light","word":"Lightly","POS":"RB","offset":0,"meanings":[]},{"term":"grease","lemma":"grease","word":"grease","POS":"NN","offset":8,"meanings":[{"definition":"a thick fatty oil (especially one used to lubricate machinery)","meaning":"grease_n_01"},{"definition":"the state of being covered with unclean things","meaning":"dirt_n_02"},{"definition":"a thick fatty oil (especially one used to lubricate machinery)","meaning":"grease_n_01"}]},{"term":"the","lemma":"the","word":"the","POS":"DT","offset":15,"meanings":[]},{"term":"pan","lemma":"pan","word":"pan","POS":"NN","offset":19,"meanings":[{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"},{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"},{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"}]},{"term":"with","lemma":"with","word":"with","POS":"IN","offset":23,"meanings":[]},{"term":"butter","lemma":"butter","word":"butter","POS":"NN","offset":28,"meanings":[{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"},{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"},{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"}]},{"term":"or","lemma":"or","word":"or","POS":"CC","offset":35,"meanings":[]},{"term":"cooking","lemma":"cooking","word":"cooking","POS":"JJ","offset":38,"meanings":[{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"},{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"},{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"}]},{"term":"spray","lemma":"spray","word":"spray","POS":"NN","offset":46,"meanings":[{"definition":"a jet of vapor","meaning":"spray_n_06"},{"definition":"a jet of vapor","meaning":"spray_n_06"},{"definition":"a pesticide in suspension or solution; intended for spraying","meaning":"spray_n_01"}]},{"term":".","lemma":".","word":".","POS":".","offset":51,"meanings":[]}],"scores":[0.3550889426044858,0.33551600342819754,0.3093950539673166]}]'
		self.result = DisambiguationResult(self.json)
		self.variant_sentences = self.result.sentences()[0].variants()
		self.variants = self.result.variants()

	def test_should_have_three_variant_sentences(self):
		self.assertEqual(3, len(self.variant_sentences))
		
	def test_should_have_three_variants(self):
		self.assertEqual(3, len(self.variants))
		
	def test_first_variant_sentence(self):
		first_variant = self.variant_sentences[0]
		self.assertEqual(10, len(first_variant.resolved_terms))

		grease = first_variant.resolved_terms[1]
		self.assertEqual("grease_n_01", grease.meaning.meaning())
		self.assertAlmostEqual(0.66, grease.score, 2)

		pan = first_variant.resolved_terms[3]
		self.assertEqual("pan_n_01", pan.meaning.meaning())
		self.assertAlmostEqual(1.0, pan.score, 2)

		self.assertEquals(u'Lightly grease_n_01 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 .', first_variant.__str__())
		self.assertEquals(u'Lightly grease_n_01 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 .', self.variants[0].__str__())

	def test_second_variant_sentence(self):
		second_variant = self.variant_sentences[1]
		self.assertEqual(10, len(second_variant.resolved_terms))

		dirt = second_variant.resolved_terms[1]
		self.assertEqual("dirt_n_02", dirt.meaning.meaning())
		self.assertAlmostEqual(0.335, dirt.score, 2)

		pan = second_variant.resolved_terms[3]
		self.assertEqual("pan_n_01", pan.meaning.meaning())
		self.assertAlmostEqual(1.0, pan.score, 2)

		self.assertEquals(u'Lightly dirt_n_02 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 .', second_variant.__str__())
		self.assertEquals(u'Lightly dirt_n_02 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 .', self.variants[1].__str__())

class TestSentenceVariantsWithOneMeaning(unittest.TestCase):

	def setUp(self):
		# "Reset the black box"
		self.json = u'[{"terms":[{"term":"Reset","lemma":"Reset","word":"Reset","POS":"VB","offset":0,"meanings":[{"definition":"device for resetting instruments or controls","meaning":"reset_n_01"}]},{"term":"the","lemma":"the","word":"the","POS":"DT","offset":6,"meanings":[]},{"term":"black box","lemma":"black_box","word":"black_box","POS":"NN","offset":10,"meanings":[{"definition":"equipment that records information about the performance of an aircraft during flight","meaning":"black_box_n_01"}]}],"scores":[1.0]}]'
		self.result = DisambiguationResult(self.json)
		self.variants = self.result.variants()
		self.variant_sentences = self.result.sentences()[0].variants()

	def test_first_sentence_should_have_one_variant_sentence(self):
		self.assertEqual(1, len(self.variant_sentences))

	def test_should_have_one_variant(self):
		self.assertEqual(1, len(self.variants))

	def test_first_variant_sentence(self):
		first_variant = self.variant_sentences[0]
		self.assertEqual(3, len(first_variant.resolved_terms))

		black_box = first_variant.resolved_terms[2]
		self.assertEqual("black_box_n_01", black_box.meaning.meaning())
		self.assertAlmostEqual(1.0, black_box.score, 2)
		
		self.assertEquals(u'reset_n_01 the black_box_n_01', first_variant.__str__())
		self.assertEquals(u'reset_n_01 the black_box_n_01', self.variants[0].__str__())

class TestSentenceVariantsWithNoMeanings(unittest.TestCase):

	def setUp(self):
		# "Go forth"
		self.json = u'[{"terms":[{"term":"Go","lemma":"go","word":"Go","POS":"VB","offset":0,"meanings":[]},{"term":"forth","lemma":"forth","word":"forth","POS":"RB","offset":3,"meanings":[]}],"scores":[]}]'
		self.result = DisambiguationResult(self.json)
		self.variants = self.result.variants()
		self.variant_sentences = self.result.sentences()[0].variants()

	def test_should_have_one_variant(self):
		self.assertEqual(1, len(self.variants))

	def test_first_sentence_should_have_one_variant_sentence(self):
		self.assertEqual(1, len(self.variant_sentences))

	def test_first_variant_sentence(self):
		first_variant = self.variant_sentences[0]
		self.assertEqual(2, len(first_variant.resolved_terms))

		self.assertEquals(u'Go forth', first_variant.__str__())
		self.assertEquals(u'Go forth', self.variants[0].__str__())

class TestVariantsWithMultipleSentencesOfVariedNumberOfVariants(unittest.TestCase):

	def setUp(self):
		# "Go forth. Reset the black box. Lightly grease the pan with butter or cooking spray."
		self.json = u'[{"terms":[{"term":"Go","lemma":"go","word":"Go","POS":"VB","offset":0,"meanings":[]},{"term":"forth","lemma":"forth","word":"forth","POS":"RB","offset":3,"meanings":[]},{"term":".","lemma":".","word":".","POS":".","offset":8,"meanings":[]}],"scores":[]},{"terms":[{"term":"Reset","lemma":"Reset","word":"Reset","POS":"VB","offset":10,"meanings":[{"definition":"device for resetting instruments or controls","meaning":"reset_n_01"}]},{"term":"the","lemma":"the","word":"the","POS":"DT","offset":16,"meanings":[]},{"term":"black box","lemma":"black_box","word":"black_box","POS":"NN","offset":20,"meanings":[{"definition":"equipment that records information about the performance of an aircraft during flight","meaning":"black_box_n_01"}]},{"term":".","lemma":".","word":".","POS":".","offset":29,"meanings":[]}],"scores":[1.0]},{"terms":[{"term":"Lightly","lemma":"light","word":"Lightly","POS":"RB","offset":31,"meanings":[]},{"term":"grease","lemma":"grease","word":"grease","POS":"NN","offset":39,"meanings":[{"definition":"a thick fatty oil (especially one used to lubricate machinery)","meaning":"grease_n_01"},{"definition":"the state of being covered with unclean things","meaning":"dirt_n_02"},{"definition":"a thick fatty oil (especially one used to lubricate machinery)","meaning":"grease_n_01"}]},{"term":"the","lemma":"the","word":"the","POS":"DT","offset":46,"meanings":[]},{"term":"pan","lemma":"pan","word":"pan","POS":"NN","offset":50,"meanings":[{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"},{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"},{"definition":"cooking utensil consisting of a wide metal vessel","meaning":"pan_n_01"}]},{"term":"with","lemma":"with","word":"with","POS":"IN","offset":54,"meanings":[]},{"term":"butter","lemma":"butter","word":"butter","POS":"NN","offset":59,"meanings":[{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"},{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"},{"definition":"an edible emulsion of fat globules made by churning milk or cream; for cooking and table use","meaning":"butter_n_01"}]},{"term":"or","lemma":"or","word":"or","POS":"CC","offset":66,"meanings":[]},{"term":"cooking","lemma":"cooking","word":"cooking","POS":"JJ","offset":69,"meanings":[{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"},{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"},{"definition":"the act of preparing something (as food) by the application of heat","meaning":"cooking_n_01"}]},{"term":"spray","lemma":"spray","word":"spray","POS":"NN","offset":77,"meanings":[{"definition":"a jet of vapor","meaning":"spray_n_06"},{"definition":"a jet of vapor","meaning":"spray_n_06"},{"definition":"a pesticide in suspension or solution; intended for spraying","meaning":"spray_n_01"}]},{"term":".","lemma":".","word":".","POS":".","offset":82,"meanings":[]}],"scores":[0.3550889426044858,0.33551600342819754,0.3093950539673166]}]'
		self.result = DisambiguationResult(self.json)
		self.sentences = self.result.sentences()
		self.variants = self.result.variants()

	def test_should_have_different_number_of_variant_sentences_for_each_sentence(self):
		self.assertEqual(1, len(self.sentences[0].variants()))
		self.assertEqual(1, len(self.sentences[1].variants()))
		self.assertEqual(3, len(self.sentences[2].variants()))

	def test_should_have_three_variants(self):
		self.assertEqual(3, len(self.variants))

	def test_variant_strings(self):
		self.assertEqual(u'Go forth . reset_n_01 the black_box_n_01 . Lightly grease_n_01 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 .', self.variants[0].__str__())
		self.assertEqual(u'Go forth . reset_n_01 the black_box_n_01 . Lightly dirt_n_02 the pan_n_01 with butter_n_01 or cooking_n_01 spray_n_06 .', self.variants[1].__str__())

if __name__ == '__main__':
    unittest.main()