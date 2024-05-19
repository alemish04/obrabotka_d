import json
import xml.etree.ElementTree as ET
import pandas as pd
import pickle

# Загрузка данных из JSON файла
with open('addres-book.json', 'r', encoding='utf-8') as file:
    address_book = json.load(file)

# Извлечение и вывод email
emails = [entry['email'] for entry in address_book]
print("Email addresses:", emails)

# Извлечение и вывод телефонов
phones = [phone['phone'] for entry in address_book for phone in entry['phones']]
print("Phone numbers:", phones)

# Загрузка данных из XML файла
tree = ET.parse('addres-book-q.xml')
root = tree.getroot()

# Формирование списка словарей с телефонами каждого человека
phone_book = []
for country in root.findall('country'):
    for address in country.findall('address'):
        person = {
            'name': address.find('name').text,
            'phones': [phone.text for phone in address.find('phones').findall('phone')]
        }
        phone_book.append(person)

print(phone_book)

# Загрузка данных из JSON файла
with open('contributors_sample.json', 'r', encoding='utf-8') as file:
    contributors = json.load(file)

# Вывод информации о первых 3 пользователях
print(contributors[:3])

unique_domains = set()
for contributor in contributors:
    email = contributor['mail']
    domain = email.split('@')[1]
    unique_domains.add(domain)

print("Unique email domains:", unique_domains)

def find_contributor_by_username(username):
    for contributor in contributors:
        if contributor['username'] == username:
            return contributor
    raise ValueError(f"User with username '{username}' not found")

# Пример использования
try:
    print(find_contributor_by_username('uhebert'))
except ValueError as e:
    print(e)

sex_count = {'M': 0, 'F': 0}
for contributor in contributors:
    sex = contributor['sex']
    if sex in sex_count:
        sex_count[sex] += 1

print("Sex count:", sex_count)

# Создание DataFrame
contributors_df = pd.DataFrame(contributors, columns=['id', 'username', 'sex'])
print(contributors_df.head())

# Загрузка данных из CSV файла
recipes = pd.read_csv('recipes_sample.csv')

# Объединение таблиц
merged_df = recipes.merge(contributors_df, how='left', left_on='contributor_id', right_on='id')

# Количество человек, для которых отсутствует информация
missing_info_count = merged_df['username'].isna().sum()
print(f"Количество человек, для которых отсутствует информация: {missing_info_count}")

job_people = {}
for contributor in contributors:
    for job in contributor['jobs']:
        if job not in job_people:
            job_people[job] = []
        job_people[job].append(contributor['username'])

print(job_people)

# Сохранение в pickle файл
with open('job_people.pickle', 'wb') as file:
    pickle.dump(job_people, file)

# Сохранение в JSON файл
with open('job_people.json', 'w', encoding='utf-8') as file:
    json.dump(job_people, file, ensure_ascii=False, indent=4)

# Чтение из pickle файла
with open('job_people.pickle', 'rb') as file:
    job_people_from_pickle = pickle.load(file)

print(job_people_from_pickle)

# Загрузка данных из XML файла
tree = ET.parse('steps_sample.xml')
root = tree.getroot()

# Формирование словаря с шагами по каждому рецепту
steps_dict = {}
for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    steps = [step.text for step in recipe.find('steps').findall('step')]
    steps_dict[recipe_id] = steps

# Сохранение в JSON файл
with open('steps_sample.json', 'w', encoding='utf-8') as file:
    json.dump(steps_dict, file, ensure_ascii=False, indent=4)

steps_count_dict = {}
for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    steps_count = len(recipe.find('steps').findall('step'))
    if steps_count not in steps_count_dict:
        steps_count_dict[steps_count] = []
    steps_count_dict[steps_count].append(recipe_id)

print(steps_count_dict)

recipes_with_time = []
for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    for step in recipe.find('steps').findall('step'):
        if 'has_minutes' in step.attrib or 'has_degrees' in step.attrib:
            recipes_with_time.append(recipe_id)
            break

print(recipes_with_time)

# Загрузка данных из CSV файла
recipes = pd.read_csv('recipes_sample.csv')

# Обновление столбца n_steps
for recipe in root.findall('recipe'):
    recipe_id = int(recipe.find('id').text)
    steps_count = len(recipe.find('steps').findall('step'))
    recipes.loc[recipes['id'] == recipe_id, 'n_steps'] = recipes.loc[recipes['id'] == recipe_id, 'n_steps'].fillna(steps_count)

print(recipes)

if recipes['n_steps'].isna().sum() == 0:
    recipes['n_steps'] = recipes['n_steps'].astype(int)
    recipes.to_csv('recipes_sample_with_filled_nsteps.csv', index=False)
    print("Файл сохранен: recipes_sample_with_filled_nsteps.csv")
else:
    print("Столбец n_steps содержит пропуски")
