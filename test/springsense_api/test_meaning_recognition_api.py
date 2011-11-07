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

if __name__ == '__main__':
    unittest.main()