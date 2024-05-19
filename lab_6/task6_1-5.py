# Importing necessary libraries
import pandas as pd
import xml.etree.ElementTree as ET
import re

# ------------------------------ PART 1 ------------------------------
print("\n\033[1mPART 1\033[0m\n")

# Load data
recipes = pd.read_csv('recipes_sample.csv')

# Select 5 random recipes
random_recipes = recipes.sample(5)

# Compute maximum column widths
id_width = max(random_recipes['id'].astype(str).map(len).max(), len('id'))
minutes_width = max(random_recipes['minutes'].astype(str).map(len).max(), len('minutes'))

# Formatting strings for the table
table_format = "|{:^" + str(id_width) + "}|{:^" + str(minutes_width) + "}|\n" + "" * (id_width + minutes_width + 3)
output = table_format.format("id", "minutes")

# Adding rows to the output
for _, row in random_recipes.iterrows():
    output += table_format.format(row['id'], row['minutes'])

print(output)

# ------------------------------ PART 2 ------------------------------
print("\n\033[1mPART 2\033[0m\n")

# Load data from CSV
recipes_df = pd.read_csv('recipes_sample.csv')

# Load data from XML
tree = ET.parse('steps_sample.xml')
root = tree.getroot()

# Dictionary to store cooking steps
steps_dict = {}

# Traverse all recipes in XML
for recipe in root.findall('recipe'):
    recipe_id = int(recipe.find('id').text)
    steps = [step.text for step in recipe.find('steps')]
    steps_dict[recipe_id] = steps

# Add cooking steps to DataFrame
recipes_df['steps'] = recipes_df['id'].map(steps_dict)

# Function to format recipe information
def show_info(name, steps, minutes, author_id):
    # Format recipe name
    title = name.title()

    # Format cooking steps
    steps_str = "\\n".join([f"{i + 1}. {step}" for i, step in enumerate(steps)])

    # Format author and cooking time information
    info = f"----------\\nАвтор: {author_id}\\nСреднее время приготовления: {minutes} минут"

    # Assemble final string
    result = f"\"{title}\"\\n\\n{steps_str}\\n{info}"

    return result

# Select recipe by ID and display its information
recipe = recipes_df[recipes_df['id'] == 170895].iloc[0]
info = show_info(recipe['name'], recipe['steps'], recipe['minutes'], recipe['contributor_id'])

# Display information with better formatting

# Вывод информации с лучшим форматированием
print(info.replace("\\n", "\n"))


# ------------------------------ PART 3 ------------------------------
print("\n\033[1mPART 3\033[0m\n")

# Load data from XML
tree = ET.parse('steps_sample.xml')
root = tree.getroot()

# Dictionary to store cooking steps
steps_dict = {}

# Traverse all recipes in XML
for recipe in root.findall('recipe'):
    recipe_id = int(recipe.find('id').text)
    steps = [step.text for step in recipe.find('steps')]
    steps_dict[recipe_id] = steps

# Regular expression to search for pattern
pattern = re.compile(r'\d+\s+(hour|hours|minute|minutes)')

# Search for pattern in each step of each recipe, starting from id 25082
for recipe_id in sorted(steps_dict.keys()):
    if recipe_id < 25082:
        continue
    steps = steps_dict[recipe_id]
    for step in steps:
        match = pattern.findall(step)
        if match:
            print(f"Recipe ID: {recipe_id}, Matches: {match}")

# ------------------------------ PART 4 ------------------------------
print("\n\033[1mPART 4\033[0m\n")

# Load data
recipes = pd.read_csv('recipes_sample.csv')

# Regular expression to search for pattern
pattern = re.compile(r"^this[\w\s\d_]*\.\.\., but")

# Search for pattern in the description of each recipe
matches = recipes['description'].str.contains(pattern, na=False)

# Select recipes for which a match is found
matching_recipes = recipes[matches]

# Display the number of matching recipes and 3 example descriptions
print(f"Количество рецептов, содержащих указанный шаблон: {len(matching_recipes)}")
print("Примеры описаний:")
for description in matching_recipes['description'].head(3):
    print(description)

# ------------------------------ PART 5 ------------------------------
print("\n\033[1mPART 5\033[0m\n")

# Load data from XML
tree = ET.parse('steps_sample.xml')
root = tree.getroot()

# Dictionary to store cooking steps
steps_dict = {}

# Traverse all recipes in XML
for recipe in root.findall('recipe'):
    recipe_id = int(recipe.find('id').text)
    steps = [step.text for step in recipe.find('steps')]
    steps_dict[recipe_id] = steps

# Regular expression to search for and replace fractions
pattern = re.compile(r'\s*/\s*')

# Search for and replace fractions in each step of recipe with id 72367
steps = steps_dict[72367]
new_steps = [pattern.sub('/', step) for step in steps]

# Display modified steps
for step in new_steps:
    print(step)
