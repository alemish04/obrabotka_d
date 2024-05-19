import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
average_ratings = np.load('average_ratings.npy')

# Данные о рецептах и их индексы
recipes_info = {
    0: 'waffle iron french toast',
    1: 'zwetschgenkuchen bavarian plum cake',
    2: 'lime tea'
}

# Построение графика
plt.figure(figsize=(10, 6))

for i in range(len(average_ratings)):
    plt.plot(average_ratings[i], label=recipes_info[i])

# Добавление подписей
plt.xlabel('Номер дня')
plt.ylabel('Средний рейтинг')
plt.title('Изменение среднего рейтинга трех рецептов')
plt.legend()
plt.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Создание диапазона дат
dates = pd.date_range(start='2019-01-01', end='2021-12-30', freq='D')

# Загрузка данных
average_ratings = np.load('average_ratings.npy')

# Данные о рецептах и их индексы
recipes_info = {
    0: 'waffle iron french toast',
    1: 'zwetschgenkuchen bavarian plum cake',
    2: 'lime tea'
}

# Построение графика
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(average_ratings)):
    ax.plot(dates, average_ratings[i], label=recipes_info[i])

# Добавление подписей
plt.xlabel('Дата')
plt.ylabel('Средний рейтинг')
plt.title('Изменение среднего рейтинга трех рецептов с разделением по годам и месяцам')
plt.legend()
plt.grid(True)

# Настройка осей
ax.xaxis.set_major_locator(plt.MaxNLocator(7))  # Отображение 7 основных делений
ax.xaxis.set_minor_locator(plt.AutoLocator())  # Добавление делений для каждого месяца

plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
average_ratings = np.load('average_ratings.npy')

# Данные о рецептах и их индексы
recipes_info = {
    0: 'waffle iron french toast',
    1: 'zwetschgenkuchen bavarian plum cake',
    2: 'lime tea'
}

# Построение графиков
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

for i, ax in enumerate(axs):
    ax.plot(average_ratings[i], label=recipes_info[i])
    ax.set_title(recipes_info[i])
    ax.set_xlabel('Номер дня')
    ax.set_ylabel('Средний рейтинг')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
visitors = np.load('visitors.npy')

# Создание диапазона дней
days = np.arange(1, len(visitors) + 1)

# Построение графиков
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Линейный масштаб
axs[0].plot(days, visitors)
axs[0].axhline(y=100, color='red', linestyle='--')
axs[0].text(80, 110, 'y(x)=100', color='red')
axs[0].set_title('Линейный масштаб')
axs[0].set_xlabel('Количество дней с момента акции')
axs[0].set_ylabel('Число посетителей')

# Логарифмический масштаб
axs[1].plot(days, visitors)
axs[1].axhline(y=100, color='red', linestyle='--')
axs[1].text(80, 110, 'y(x)=100', color='red')
axs[1].set_yscale('log')
axs[1].set_title('Логарифмический масштаб')
axs[1].set_xlabel('Количество дней с момента акции')
axs[1].set_ylabel('Число посетителей')

plt.suptitle('Изменение количества пользователей в линейном и логарифмическом масштабе', fontsize=16)
plt.show()
