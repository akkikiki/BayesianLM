# coding: utf-8

import sys
import numpy as np
import read_corpus

# need P(z_i|z_-i, w)
# z_{-i}: the count that does not include z_i
# output: perplexity
# current implementation refers to shuyo-san's blog

class GibbsSampler:

    def __init__(self):
        beta = 0.5
        self.D = read_corpus.read_corpus()
        self.K = 2
        self.V = 10000 # TODO: need to be revised, size of the vocab.
        self.z_mn = self.init(self.D, self.K)
        self.n_tz = np.zeros((self.K, self.V)) + beta
        # what are the topics assigned a single word?
        # makes the K * D matrix, K: # of topics, D:

    def init(self, D, K):

        z_mn = [] # topics of words for each document 
        for document in D:
            z = np.random.randint(0, K, len(document))
            z_mn.append(z) # keep it as a matrix
        return z_mn
    
    def infer_topic(self, D, document_topics):
        for doc_num in range(len(D)):
            z_w = self.z_mn[doc_num] # topics for one document
            words = D[doc_num]
            for i in range(len(z_w)):
                t = words[i]
                # exclude the current topic z that we are focusing on 
                old_z = z_w[i]
                n_z[z] -= 1
                n_tz[t][z] -= 1
                n_mz[m][z] -= 1 #
    
                p_z = n_z_t[:, t] * n_mz[m] / self.n_z
                new_z = numpy.random.multinomial(1, p_z / p_z.sum()).argmax()
                z_w.append(new_z) # adding new inferred topic for one word
    
        # what is the i here?
                p_z = (n_mz[m][z] * alpha) * ( (n_tz[m][n] + beta) / ( (sum(n_d) - n_d[i]) + T * beta) ) 
    
    
    # To simplify, let's assume that T=2 and W=2
    def gibbs_sampler(K, D):
        """ K: Num. of topics (given beforehand)
            D: arrays of words each indice represent one document (Let's assume that we have only two documents)
        """ 
        z_m = [] # topics for each document
        z_mn = [] # topics of words for each document, 
        n_mz = [[]] # number of times a document m has been assigned to topic j
        n_tz = [[]] # num. of times a word t that has been assigned to topic z, row: t, column:z
        n_z = [] # num. of words that has topic z
    
        n_d = [] #
    
        # As an initialization, assign a random topic to individual words
        z_mn = init(D, K)
    
    def calculate_multinomial_distribution(n, beta, alpha, W=2, T=2):
        p_w_j = n_topic_i

if __name__ == "__main__":
    D = read_corpus.read_corpus()
    K = 4
    init(D, K)
