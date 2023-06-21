from main import all_words, word_vectors
import random


def get_idx_distance(_word, target_word, _similarity_vector):
    if _word == target_word:
        return -1

    for idx, i in enumerate(_similarity_vector):
        if i[0] == _word:
            return idx


class ContextoGame:

    def __init__(self):
        self.day_word = random.choice(all_words)

    @staticmethod
    def get_idx_distance(_word, target_word, _similarity_vector):
        if _word == target_word:
            return -1

        for idx, i in enumerate(_similarity_vector):
            if i[0] == _word:
                return idx

    def guess(self, guess):

        words = []
        similarity_vector = word_vectors.similar_by_word(self.day_word, topn=len(word_vectors.index_to_key))

        distance = get_idx_distance(guess, self.day_word, similarity_vector)

        return distance
        # if distance == -1:
        #     print("ACERTOU")
        # else:
        #     words.append(f'{guess} ---------- {distance}')
        #     for x in words:
        #         print(x)
