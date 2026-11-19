import math

class CountVectorizer:

    def __init__(self, lowercase=True, ngram_size=1):
        self.vocabulary = {}
        self.ngram_size = ngram_size
        self.lowercase = lowercase

    @property
    def vocabulary(self):
        return self._vocabulary

    @vocabulary.setter
    def vocabulary(self, value):
        self._vocabulary = value

    @vocabulary.deleter
    def vocabulary(self):
        self._vocabulary = {}


    def add_word(self, word):
        words = self.vocabulary
        if word not in self.vocabulary:
            words[word] = len(self.vocabulary)
        return self.vocabulary[word]

    
    def tokenize(self, text):
        after_split = []
        if self.lowercase:
            text = text.lower()
        text = text.split()
        if self.ngram_size == 1:
            return text
        elif self.ngram_size == 2:
            for i in range(0, len(text) - 1):
                after_split.append(text[i] + " " + text[i + 1])
            return after_split

    def fit(self, corpus):
        old_vocabulary = self.vocabulary
        self.vocabulary = {}
        for i in range(len(corpus)):
            tokens = self.tokenize(corpus[i])
            for j in range(len(tokens)):
                self.add_word(tokens[j])
        if len(self.vocabulary) == 0:
            self.vocabulary = old_vocabulary
            raise ValueError
        return self

    def transform(self, corpus):
        if len(self.vocabulary) == 0:
            raise RuntimeError
        freq_matrix = []
        for i in range(len(corpus)):
            row = [0] * len(self.vocabulary)
            tokens = self.tokenize(corpus[i])
            for j in range(len(tokens)):
                if tokens[j] in self.vocabulary:
                    row[self.vocabulary[tokens[j]]] += 1
            freq_matrix.append(row)
        return freq_matrix

    def get_feature_names(self):
        names = [""] * len(self.vocabulary)
        for word in self.vocabulary:
            names[self.vocabulary[word]] = word
        return names

    def fit_transform(self, corpus):
        return self.fit(corpus).transform(corpus)

    def to_dict(self):
        return {
            "lowercase": self.lowercase,
            "ngram_size": self.ngram_size,
            "vocabulary": self.vocabulary.copy(),
        }

    @classmethod
    def from_dict(cls, state):
        vectorizer = cls(lowercase=state["lowercase"], ngram_size=state["ngram_size"])
        vectorizer.vocabulary = state["vocabulary"].copy()
        return vectorizer

class BinaryVectorizer(CountVectorizer):
    def transform(self, corpus):
        freq_matrix = super().transform(corpus)
        for i in range(len(freq_matrix)):
            for j in range(len(freq_matrix[i])):
                if freq_matrix[i][j] > 0:
                    freq_matrix[i][j] = 1
                else:
                    freq_matrix[i][j] = 0
        return freq_matrix

class TfidfVectorizer(CountVectorizer):

    def __init__(self, lowercase=True, use_idf=True):
        super().__init__(lowercase=lowercase)
        self.use_idf = use_idf
        self._idf = []

    def fit(self, corpus):
        super().fit(corpus)
        if not self.use_idf:
            self._idf = []
            return self
        else:
            df = [0] * len(self.vocabulary)
            for i in range(len(corpus)):
                seen = set()
                tokens = self.tokenize(corpus[i])
                for j in range(len(tokens)):
                    if tokens[j] in self.vocabulary and tokens[j] not in seen:
                        df[self.vocabulary[tokens[j]]] += 1
                        seen.add(tokens[j])
            self._idf = []
            for j in range(len(df)):
                self._idf.append(math.log((len(corpus) + 1) / (df[j] + 1)) + 1)
            return self

    def transform(self, corpus):
        counts = super().transform(corpus)
        matrix = []
        for i in range(len(counts)):
            total = sum(counts[i])
            row = []
            for j in range(len(counts[i])):
                if total == 0:
                    row.append(0.0)
                else:
                    if self.use_idf:
                        row.append(counts[i][j] / total * self._idf[j])
                    else:
                        row.append(counts[i][j] / total)
            matrix.append(row)
        return matrix

    @classmethod
    def from_config(cls, config):
        return cls(
            lowercase=config.get("lowercase", True),
            use_idf=config.get("use_idf", True),
        )

    @property
    def idf(self):
        return self._idf.copy()


def sort_key(pair):
    return (-pair[1], pair[0])


class KeywordExtractor:

    def __init__(self, vectorizer, top_n=3):
        self.vectorizer = vectorizer
        self.top_n = top_n

    @property
    def top_n(self):
        return self._top_n

    @top_n.setter
    def top_n(self, value):
        if type(value) is not int or value <= 0:
            raise ValueError
        self._top_n = value

    def fit(self, corpus):
        self.vectorizer.fit(corpus)
        return self

    def extract(self, corpus):
        matrix = self.vectorizer.transform(corpus)
        names = self.vectorizer.get_feature_names()
        result = []
        for i in range(len(matrix)):
            pairs = []
            for j in range(len(matrix[i])):
                if matrix[i][j] > 0:
                    pairs.append((names[j], matrix[i][j]))
            pairs.sort(key=sort_key)
            result.append(pairs[:self.top_n])
        return result


# Обучающие сообщения
TRAIN_CORPUS = [
    "Марс сигнал сигнал",
    "Марс пыль",
    "Марс сигнал антенна",
]

# Сообщения для проверки
CHECK_CORPUS = [
    "СИГНАЛ шум сигнал",
    "антенна пыль",
    "марс марс марс",
    "комета",
    "",
]


def demo():
    #сценарий 1: веса TF-IDF
    print("Веса TF-IDF")

    tfidf = TfidfVectorizer.from_config({})
    train_matrix = tfidf.fit_transform(TRAIN_CORPUS)

    print("Слова:", tfidf.get_feature_names())
    print("IDF:", tfidf.idf)
    print("Матрица TRAIN_CORPUS:", train_matrix)
    print("Матрица CHECK_CORPUS:", tfidf.transform(CHECK_CORPUS))

    #т.к. idf возвращает копиб, очистка спика не изменяет веса
    idf_list = tfidf.idf
    idf_list.clear()
    print("IDF после очистки списка:", tfidf.idf)
    print()
    print()

    #сценарий 2: Настройки и новый fit()
    print("Настройки и новый fit()")

    tf = TfidfVectorizer.from_config({"lowercase": False, "use_idf": False})
    tf_matrix = tf.fit_transform(["Марс марс", "МАРС сигнал"])

    print("Слова:", tf.get_feature_names())
    print("IDF:", tf.idf)
    print("TF:", tf_matrix)


    tfidf.fit(["Венера облака"])

    print("Слова после нового fit:", tfidf.get_feature_names())
    print("IDF после нового fit:", tfidf.idf)

    print("Матрица для ['Марс Венера облака']:",
          tfidf.transform(["Марс Венера облака"]))
    print()
    print()

    #сценарий 3: ключевые слова
    print("Ключевые слова")

    extractor = KeywordExtractor(tfidf, top_n=2)
    extractor.fit(TRAIN_CORPUS)

    print("top_n=2:", extractor.extract(CHECK_CORPUS))

    extractor.top_n = 1
    print("top_n=1:", extractor.extract(CHECK_CORPUS))

    try:
        extractor.top_n = 0
    except ValueError:
        print("top_n должен быть целым числом больше 0")
    print("top_n:", extractor.top_n)


if __name__ == "__main__":
    demo()