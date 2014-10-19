import unittest
from gibbs_sampler import GibbsSampler
import read_corpus 
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        self.D = read_corpus.read_corpus()
        self.K = 4
        self.gibbs_sampler = GibbsSampler()
        self.document_topics = self.gibbs_sampler.init(self.D, self.K)
        #pass
 
    def test_infer_topic(self):
        result = self.gibbs_sampler.infer_topic(self.D, self.document_topics)
        print (result)
        #self.assertEqual( multiply('a',3), 'aaa')
 
if __name__ == '__main__':
    unittest.main()
