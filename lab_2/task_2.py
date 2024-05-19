import pandas as pd

# 1. Загрузите данные из файла `sp500hst.txt` и обозначьте столбцы в соответствии с содержимым.
columns = ["date", "ticker", "open", "high", "low", "close", "volume"]
data = pd.read_csv("sp500hst.txt", header=None, names=columns)

# 2. Рассчитайте среднее значение показателей для каждого из столбцов c номерами 3-6.
mean_values = data.iloc[:, 2:6].mean()
print("Средние значения показателей для столбцов с 3 по 6:\n", mean_values)

# 3. Добавьте столбец, содержащий только число месяца, к которому относится дата.
data['date'] = pd.to_datetime(data['date'], format='%Y%m%d')
data['day'] = data['date'].dt.day
print("Данные с добавленным столбцом 'day':\n", data.head())

# 4. Рассчитайте суммарный объем торгов для для одинаковых значений тикеров.
volume_sum = data.groupby('ticker')['volume'].sum()
print("Суммарный объем торгов для каждого тикера:\n", volume_sum)

# 5. Загрузите данные из файла `sp500hst.txt` и обозначьте столбцы в соответствии с содержимым:
#    "date", "ticker", "open", "high", "low", "close", "volume".
#    Добавьте столбец с расшифровкой названия тикера, используя данные из файла `sp_data2.csv`.
ticker_data = pd.read_csv('sp_data2.csv', sep=';', header=None, names=['ticker', 'name', 'weight'])
merged_data = data.merge(ticker_data[['ticker', 'name']], on='ticker', how='left')
print("Данные с добавленным названием тикера:\n", merged_data.head())

# Лабораторная работа №2
# 1.1 Загрузка данных из файлов `recipes_sample.csv` и `reviews_sample.csv`
recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv', index_col=0)

# 1.2 Основные параметры таблиц
def print_table_info(df, name):
    print(f"Информация о таблице {name}:")
    print("Количество строк:", df.shape[0])
    print("Количество столбцов:", df.shape[1])
    print("Типы данных каждого столбца:\n", df.dtypes)
    print()

print_table_info(recipes, 'recipes')
print_table_info(reviews, 'reviews')

# 1.3 Проверка столбцов на наличие пропусков
recipes_missing = recipes.isnull().any()
reviews_missing = reviews.isnull().any()
recipes_missing_ratio = recipes.isnull().mean().mean()
reviews_missing_ratio = reviews.isnull().mean().mean()

print("Столбцы с пропусками в таблице recipes:\n", recipes_missing)
print("Доля строк с пропусками в таблице recipes:", recipes_missing_ratio)
print("Столбцы с пропусками в таблице reviews:\n", reviews_missing)
print("Доля строк с пропусками в таблице reviews:", reviews_missing_ratio)

# 1.4 Среднее значение для каждого из числовых столбцов
# Загрузка данных
recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv')

# Проверка на пропуски
recipes_null_count = recipes.isnull().sum()
reviews_null_count = reviews.isnull().sum()

# Доля строк с пропусками
recipes_null_fraction = recipes.isnull().mean()
reviews_null_fraction = reviews.isnull().mean()

print(f"Доля строк с пропусками в таблице recipes: {recipes_null_fraction}")
print("Столбцы с пропусками в таблице reviews:")
print(reviews.isnull().any())
print(f"Доля строк с пропусками в таблице reviews: {reviews_null_fraction}")

# Расчет среднего значения для числовых столбцов
recipes_mean = recipes.select_dtypes(include='number').mean()

print("Средние значения для числовых столбцов:")
print(recipes_mean)

# 1.5 Создание серии из 10 случайных названий рецептов
random_recipes = recipes['name'].sample(10)
print("Случайные названия рецептов:\n", random_recipes)

# 1.6 Изменение индекса в таблице `reviews`
reviews.reset_index(drop=True, inplace=True)
print("Таблица reviews с измененным индексом:\n", reviews.head())

# 1.7 Информация о рецептах с временем выполнения не больше 20 минут и количеством ингредиентов не больше 5
quick_easy_recipes = recipes[(recipes['minutes'] <= 20) & (recipes['n_ingredients'] <= 5)]
print("Рецепты с временем выполнения не больше 20 минут и количеством ингредиентов не больше 5:\n", quick_easy_recipes)

# Работа с датами
# 2.1 Преобразование столбца `submitted` в формат времени
recipes['submitted'] = pd.to_datetime(recipes['submitted'])

# 2.2 Информация о рецептах, добавленных не позже 2010 года
recipes_pre_2010 = recipes[recipes['submitted'].dt.year <= 2010]
print("Рецепты, добавленные не позже 2010 года:\n", recipes_pre_2010)

# Работа со строковыми данными
# 3.1 Добавление столбца `description_length`
recipes['description_length'] = recipes['description'].str.len()
print("Таблица recipes с добавленным столбцом `description_length`:\n", recipes.head())

# 3.2 Изменение названий рецептов с прописной буквы
recipes['name'] = recipes['name'].str.title()
print("Таблица recipes с измененными названиями:\n", recipes.head())

# 3.3 Добавление столбца `name_word_count`
recipes['name_word_count'] = recipes['name'].str.split().str.len()
print("Таблица recipes с добавленным столбцом `name_word_count`:\n", recipes.head())

# Группировки таблиц
# 4.1 Количество рецептов для каждого участника
contributor_recipe_count = recipes['contributor_id'].value_counts()
max_contributor = contributor_recipe_count.idxmax()
print("Количество рецептов для каждого участника:\n", contributor_recipe_count)
print("Участник, добавивший максимальное количество рецептов:", max_contributor)

# 4.2 Средний рейтинг для каждого рецепта и количество рецептов без отзывов
recipe_avg_rating = reviews.groupby('recipe_id')['rating'].mean()
no_reviews = recipes[~recipes['id'].isin(reviews['recipe_id'])]
print("Средний рейтинг для каждого рецепта:\n", recipe_avg_rating)
print("Количество рецептов без отзывов:", len(no_reviews))

# 4.3 Количество рецептов по годам создания
recipes_per_year = recipes['submitted'].dt.year.value_counts().sort_index()
print("Количество рецептов по годам создания:\n", recipes_per_year)

# Объединение таблиц
# 5.1 Создание `DataFrame` с четырьмя столбцами: `id`, `name`, `user_id`, `rating`
recipes_with_reviews = recipes.merge(reviews, left_on='id', right_on='recipe_id')
result_5_1 = recipes_with_reviews[['id', 'name', 'user_id', 'rating']]
print("Результат объединения таблиц (5.1):\n", result_5_1.head())

# 5.2 Создание `DataFrame` с тремя столбцами: `recipe_id`, `name`, `review_count`
review_counts = reviews.groupby('recipe_id').size().reset_index(name='review_count')
result_5_2 = recipes[['id', 'name']].merge(review_counts, left_on='id', right_on='recipe_id', how='left').fillna(0)
result_5_2['review_count'] = result_5_2['review_count'].astype(int)
print("Результат объединения таблиц (5.2):\n", result_5_2.head())

# 5.3 Год с наименьшим средним рейтингом рецептов
recipes_with_reviews['year'] = recipes_with_reviews['submitted'].dt.year
average_rating_per_year = recipes_with_reviews.groupby('year')['rating'].mean()
worst_year = average_rating_per_year.idxmin()
print("Год с наименьшим средним рейтингом рецептов:", worst_year)

# Сохранение таблиц
# 6.1 Сортировка и сохранение результатов заданий 3.1-3.3 в CSV файл
sorted_recipes = recipes.sort_values(by='name_word_count', ascending=False)
sorted_recipes.to_csv('recipes_with_additional_info.csv', index=False)

# 6.2 Сохранение результатов 5.1 и 5.2 в Excel файл
with pd.ExcelWriter('recipes_reviews.xlsx') as writer:
    result_5_1.to_excel(writer, sheet_name='Рецепты с оценками', index=False)
    result_5_2.to_excel(writer, sheet_name='Количество отзывов по рецептам', index=False)
