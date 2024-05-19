import pandas as pd
import xml.etree.ElementTree as ET
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
nltk.download('punkt')

# Загрузка данных из XML
tree = ET.parse('steps_sample.xml')
root = tree.getroot()

# Словарь для хранения шагов приготовления
steps_dict = {}

# Обход всех рецептов в XML
for recipe in root.findall('recipe'):
    recipe_id = int(recipe.find('id').text)
    steps = [step.text for step in recipe.find('steps')]
    steps_dict[recipe_id] = steps

# Список для хранения всех слов
all_words = []

# Разбиение текстов шагов на слова и добавление их в список
for steps in steps_dict.values():
    for step in steps:
        words = word_tokenize(step)
        all_words.extend([word.lower() for word in words if word.isalpha()])

# Подсчет количества уникальных слов
unique_words = Counter(all_words)

# Вывод количества уникальных слов
print(f"Количество уникальных слов: {len(unique_words)}")
