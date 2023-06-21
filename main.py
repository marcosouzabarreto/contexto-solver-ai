from gensim.models.keyedvectors import KeyedVectors

print('started the word vectorization')
word_vectors = KeyedVectors.load_word2vec_format('glove_s300.txt', binary=False)
print('finished word vectorization, started creating all words list')
all_words = list(word_vectors.index_to_key)

