import pandas as pd
import nltk

# Загрузка данных
recipes = pd.read_csv('recipes_sample.csv')

# Разбиение описаний рецептов на предложения
recipes['sentences'] = recipes['description'].apply(lambda x: nltk.sent_tokenize(str(x)))

# Вычисление количества предложений в каждом описании
recipes['num_sentences'] = recipes['sentences'].apply(len)

# Выбор 5 рецептов с самыми длинными описаниями
longest_descriptions = recipes.nlargest(5, 'num_sentences')

# Вывод строк фрейма, соответствующих этим рецептам
print(longest_descriptions)
