import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.metrics.distance import edit_distance
import random
import nltk
from tqdm import trange
from termcolor import colored

print("""при первом запуске может понадобиться запустить 2 строки ниже
      nltk.download('wordnet')
      nltk.download('stopwords')""")
# nltk.download('wordnet')
# nltk.download('stopwords')

print(colored("task 1", 'red'))
print(colored("1.1", 'green'))
# a. Загрузите предобработанные описания рецептов из файла preprocessed_descriptions.csv.
df = pd.read_csv('preprocessed_descriptions.csv')

# Получите набор уникальных слов words, содержащихся в текстах описаний рецептов.
words = set(word_tokenize(' '.join(df['preprocessed_description'].astype(str))))

# b. Сгенерируйте 5 пар случайно выбранных слов и посчитайте между ними расстояние редактирования.
print("1.2")
for _ in range(5):
    word1, word2 = random.sample(list(words), 2)
    print(colored(f'Words: {word1}, {word2} - Edit distance: {edit_distance(word1, word2)}', 'blue'))

# c. Напишите функцию, которая для заданного слова word возвращает k ближайших к нему слов из списка words.
print("1.3")


def closest_words(word, words, k=5):
    distances = [(w, edit_distance(word, w)) for w in words]
    return sorted(distances, key=lambda x: x[1])[:k]


print(colored(closest_words('apple', words), 'cyan'))

from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

print(colored("task 2", 'red'))
print(colored("2.1", 'green'))
# a. Создайте pd.DataFrame со столбцами: word, stemmed_word, normalized_word.
stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()

df_words = pd.DataFrame([(word, stemmer.stem(word), lemmatizer.lemmatize(word)) for word in words],
                        columns=['word', 'stemmed_word', 'normalized_word']).set_index('word')

# b. Удалите стоп-слова из описаний рецептов.
print("2.3")
stop_words = set(stopwords.words('english'))
df['preprocessed_description'] = df['preprocessed_description'].apply(
    lambda x: ' '.join([word for word in word_tokenize(str(x)) if word not in stop_words]))
# df['preprocessed_description'] = df['preprocessed_description'].apply(lambda x: ' '.join([word for word in word_tokenize(x) if word not in stop_words]))


from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import cosine

print("task 3")
print("3.1")
# a. Выберите случайным образом 5 рецептов из набора данных.
random_recipes = df.sample(5)

# Представьте описание каждого рецепта в виде числового вектора при помощи TfidfVectorizer.
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(random_recipes['preprocessed_description'])

# b. Вычислите близость между каждой парой рецептов.
print("3.2")
distances = pd.DataFrame(index=random_recipes['name'], columns=random_recipes['name'])
for i in range(X.shape[0]):
    for j in range(X.shape[0]):
        distances.iloc[i, j] = cosine(X[i].toarray().flatten(), X[j].toarray().flatten())

print(colored(distances, 'blue'))
# Экспорт в Excel выводится полное
print(colored(
    "в консоль не выводится полная таблица, вместо этого полный результат сохранён в excel в текущей директории",
    'magenta'))
distances.to_excel("output.xlsx")
