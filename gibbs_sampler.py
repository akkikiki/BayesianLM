# coding: utf-8

import sys
import numpy as np
import read_corpus

# need P(z_i|z_-i, w)
# z_{-i}: the count that does not include z_i
# output: perplexity
# current implementation refers to shuyo-san's blog

def initialization(D, K):
    z_mn = [] # topics of words for each document 
    for document in D:
        z = np.random.randint(0, K, len(document))
        z_mn.append(z) # keep it as a matrix
    return z_mn

def infer_topic(D, document_topics):
    for document in D:
        z_w = [] # topics for one document
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
    z_mn = initialization(D, K)

def calculate_multinomial_distribution(n, beta, alpha, W=2, T=2):
    p_w_j = n_topic_i

if __name__ == "__main__":
    D = read_corpus.read_corpus()
    K = 4
    initialization(D, K)
