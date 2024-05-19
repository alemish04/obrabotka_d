import pandas as pd
import nltk

# Загрузка данных
recipes = pd.read_csv('recipes_sample.csv')
nltk.download('averaged_perceptron_tagger')

# Функция для вывода информации о частях речи слов в предложении
def print_pos(sentence):
    # Разбиение предложения на слова и определение их частей речи
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)

    # Форматирование и вывод информации о частях речи
    pos_line = ""
    words_line = ""
    for word, pos in pos_tags:
        space = " " * (len(word) - len(pos))
        pos_line += space + pos + " "
        words_line += word + " "
    print(pos_line + "\n" + words_line)


# Проверка работоспособности функции на названии рецепта с id 241106
recipe = recipes[recipes['id'] == 241106].iloc[0]
print_pos(recipe['name'])
