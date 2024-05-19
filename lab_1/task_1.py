import numpy as np
from colorama import Fore, Style

# Считывание заголовков
with open(r"C:\Users\alex_laptop\Documents\универ\заочка\технологиии обработки данных\v1\data\minutes_n_ingredients.csv", mode="r") as file:
    cols = file.readline().strip("\n").split(",")
    print(Fore.CYAN + "Заголовки: " + Style.RESET_ALL, cols)

# Считывание данных
df = np.loadtxt(r"C:\Users\alex_laptop\Documents\универ\заочка\технологиии обработки данных\v1\data\minutes_n_ingredients.csv",
                dtype="int32", skiprows=1, delimiter=",")
print(Fore.CYAN + "Первые 5 строк массива:" + Style.RESET_ALL)
print(df[:5])

# Среднее значение, минимум, максимум и медиана для второго и третьего столбцов
mean_values = np.mean(df[:, 1:], axis=0)
min_values = np.min(df[:, 1:], axis=0)
max_values = np.max(df[:, 1:], axis=0)
median_values = np.median(df[:, 1:], axis=0).astype(int)

print(f"\n{Fore.GREEN}Средние значения: {Style.RESET_ALL}{mean_values}")
print(f"{Fore.GREEN}Минимальные значения: {Style.RESET_ALL}{min_values}")
print(f"{Fore.GREEN}Максимальные значения: {Style.RESET_ALL}{max_values}")
print(f"{Fore.GREEN}Медианные значения: {Style.RESET_ALL}{median_values}")

# Квантиль 0.75 для продолжительности выполнения рецепта
q_75 = np.quantile(df[:, 1], 0.75)
print(f"\n{Fore.YELLOW}Квантиль 0.75 для продолжительности: {Style.RESET_ALL}{q_75}")

# Ограничение значений
df[:, 1] = np.minimum(df[:, 1], q_75)
print(Fore.CYAN + "Первые 5 строк массива после ограничения значений:" + Style.RESET_ALL)
print(df[:5])

# Количество рецептов с нулевой продолжительностью
zero_duration_count = np.sum(df[:, 1] == 0)
print(f"\n{Fore.RED}Количество рецептов с нулевой продолжительностью: {Style.RESET_ALL}{zero_duration_count}")

# Замена нулевых значений на 1
df[df[:, 1] == 0, 1] = 1
print(Fore.CYAN + "Первые 5 строк массива после замены нулевых значений:" + Style.RESET_ALL)
print(df[:5])

# Количество уникальных рецептов
unique_recipes_count = np.unique(df[:, 0]).size
print(f"\n{Fore.MAGENTA}Количество уникальных рецептов: {Style.RESET_ALL}{unique_recipes_count}")

# Уникальные значения количества ингредиентов и их количество
unique_ingredients, counts_ingredients = np.unique(df[:, 2], return_counts=True)
print(f"\n{Fore.BLUE}Уникальные значения количества ингредиентов и их количество:{Style.RESET_ALL}")
for ingredient, count in zip(unique_ingredients, counts_ingredients):
    print(f"Ингредиенты: {ingredient}, Количество: {count}")

# Рецепты с не более чем 5 ингредиентами
recipes_le_5_ingredients = df[df[:, 2] <= 5]
print(f"\n{Fore.CYAN}Рецепты с не более чем 5 ингредиентами:{Style.RESET_ALL}\n", recipes_le_5_ingredients)

# Среднее количество ингредиентов на одну минуту и максимальное значение
ingredients_per_minute = df[:, 2] / df[:, 1]
max_ingredients_per_minute = np.max(ingredients_per_minute)
print(f"\n{Fore.GREEN}Максимальное среднее количество ингредиентов на одну минуту: {Style.RESET_ALL}{max_ingredients_per_minute:.2f}")

# Среднее количество ингредиентов для топ-100 рецептов с наибольшей продолжительностью
top_100_recipes = df[np.argsort(df[:, 1])[-100:]]
mean_ingredients_top_100 = np.mean(top_100_recipes[:, 2])
print(f"\n{Fore.GREEN}Среднее количество ингредиентов для топ-100 рецептов с наибольшей продолжительностью: {Style.RESET_ALL}{mean_ingredients_top_100:.2f}")

# Случайный выбор 10 различных рецептов
random_indices = np.random.choice(df.shape[0], 10, replace=False)
random_recipes = df[random_indices]
print(f"\n{Fore.CYAN}Случайный выбор 10 различных рецептов:{Style.RESET_ALL}\n", random_recipes)

# Процент рецептов с количеством ингредиентов меньше среднего
mean_ingredients = np.mean(df[:, 2])
percent_less_than_mean = np.sum(df[:, 2] < mean_ingredients) / df.shape[0] * 100
print(f"\n{Fore.GREEN}Процент рецептов с количеством ингредиентов меньше среднего: {Style.RESET_ALL}{percent_less_than_mean:.2f}%")

# Простой рецепт
simple_recipes = np.where((df[:, 1] <= 20) & (df[:, 2] <= 5), 1, 0)
df_with_simple = np.hstack((df, simple_recipes.reshape(-1, 1)))
print(f"\n{Fore.CYAN}Массив с признаком простого рецепта:{Style.RESET_ALL}\n", df_with_simple[:5])

# Процент простых рецептов
percent_simple_recipes = np.sum(simple_recipes) / df.shape[0] * 100
print(f"\n{Fore.GREEN}Процент простых рецептов: {Style.RESET_ALL}{percent_simple_recipes:.2f}%")

# Группировка рецептов
short_recipes = df[df[:, 1] < 10]
standard_recipes = df[(df[:, 1] >= 10) & (df[:, 1] < 20)]
long_recipes = df[df[:, 1] >= 20]

# Определение максимального количества рецептов в каждой группе
max_group_size = min(len(short_recipes), len(standard_recipes), len(long_recipes))

# Создание трехмерного массива
three_dimensional_array = np.array([
    short_recipes[:max_group_size],
    standard_recipes[:max_group_size],
    long_recipes[:max_group_size]
])

print(f"\n{Fore.MAGENTA}Форма трехмерного массива: {Style.RESET_ALL}{three_dimensional_array.shape}")
