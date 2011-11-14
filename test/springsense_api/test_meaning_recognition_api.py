import unittest
from springsense_api.meaning_recognition_api import MeaningRecognitionAPI

class TestMeaningRecognitionAPI(unittest.TestCase):
	
	def setUp(self):
		self.api = MeaningRecognitionAPI("http://172.31.1.235:8080")
		
	def test_should_initialize_correctly(self):
		self.assertEquals("http://172.31.1.235:8080", self.api.url)

	def test_recognize_should_return_result(self):
		expected_result = u'[{"terms":[{"term":"cat","lemma":"cat","word":"cat","POS":"NN","offset":0,"meanings":[{"definition":"feline mammal usually having thick soft fur and no ability to roar: domestic cats; wildcats","meaning":"cat_n_01"},{"definition":"any of several large cats typically able to roar and living in the wild","meaning":"big_cat_n_01"},{"definition":"any of several large cats typically able to roar and living in the wild","meaning":"big_cat_n_01"}]},{"term":"vet","lemma":"vet","word":"vet","POS":"NN","offset":4,"meanings":[{"definition":"a doctor who practices veterinary medicine","meaning":"veterinarian_n_01"},{"definition":"a person who has served in the armed forces","meaning":"veteran_n_02"},{"definition":"a doctor who practices veterinary medicine","meaning":"veterinarian_n_01"}]}],"scores":[0.3348004418567183,0.33266345412226733,0.33253610402101424]}]'
		result = self.api.recognize("cat vet")
		self.assertEqual(expected_result, result.json)
		self.assertEquals(u'cat_n_01 veterinarian_n_01', result.variants()[0].__str__())

	def test_recognize_should_return_result_with_percent_sign(self):
		expected_result = u'[{"terms":[{"term":"black box","lemma":"black_box","word":"black_box","POS":"NN","offset":0,"meanings":[{"definition":"equipment that records information about the performance of an aircraft during flight","meaning":"black_box_n_01"},{"definition":"equipment that records information about the performance of an aircraft during flight","meaning":"black_box_n_01"},{"definition":"equipment that records information about the performance of an aircraft during flight","meaning":"black_box_n_01"}]},{"term":"%","lemma":"%","word":"%","POS":"NNP","offset":10,"meanings":[]},{"term":"failure","lemma":"failure","word":"failure","POS":"NN","offset":12,"meanings":[{"definition":"an act that fails","meaning":"failure_n_01"},{"definition":"an event that does not accomplish its intended purpose","meaning":"failure_n_02"},{"definition":"loss of ability to function normally","meaning":"failure_n_07"}]}],"scores":[0.340135213013422,0.33047046238172023,0.3293943246048579]}]'
		result = self.api.recognize("black box % failure")
		self.assertEqual(expected_result, result.json)
		self.assertEquals(u'black_box_n_01 % failure_n_01', result.variants()[0].__str__())

	def test_recognize_should_work_with_unicode_characters(self):
		expected_result = u'[{"terms":[{"term":"black box","lemma":"black_box","word":"black_box","POS":"NN","offset":0,"meanings":[{"definition":"equipment that records information about the performance of an aircraft during flight","meaning":"black_box_n_01"}]},{"term":"\u2013","lemma":"\u2013","word":"\u2013","POS":"\u2013","offset":10,"meanings":[]},{"term":"was","lemma":"be","word":"was","POS":"VBD","offset":12,"meanings":[]},{"term":"here","lemma":"here","word":"here","POS":"RB","offset":16,"meanings":[]}],"scores":[1.0]}]'
		result = self.api.recognize(u'black box \u2013 was here')
		self.assertEqual(expected_result, result.json)
		self.assertEquals(u'black_box_n_01 \u2013 was here', result.variants()[0].__str__())

if __name__ == '__main__':
    unittest.main()