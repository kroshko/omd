class CountVectorizer:
    def __init__(self):
        self.feature_names = []

    def fit_transform(self, corpus):
        unique_words = set()
        for document in corpus:
            words = document.lower().split()
            unique_words.update(words)
        self.feature_names = sorted(list(unique_words))
        count_matrix = []
        for document in corpus:
            words = document.lower().split()
            word_count = [words.count(word) for word in self.feature_names]
            count_matrix.append(word_count)
        return count_matrix

    def get_feature_names(self):
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
