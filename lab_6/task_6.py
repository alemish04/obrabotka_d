import pandas as pd

# Load data from recipes_sample.csv
recipes = pd.read_csv("recipes_sample.csv")

# Displaying id and minutes for 5 random recipes
print(recipes[['id', 'minutes']].sample(5))


import xml.etree.ElementTree as ET

def show_info(name, steps, minutes, author_id):
    # Constructing the string description
    description = f"\"{name.title()}\"\n\n"
    for i, step in enumerate(steps, start=1):
        description += f"{i}. {step}\n"
    description += "----------\n"
    description += f"Author: {author_id}\n"
    description += f"Average cooking time: {minutes} minutes\n"
    return description

# Parsing XML file
tree = ET.parse("steps_sample.xml")
root = tree.getroot()

# Extracting data for recipe with id 170895
recipe_id = "170895"
name = root.find(f"./recipe[id='{recipe_id}']/name").text
steps = [step.text for step in root.find(f"./recipe[id='{recipe_id}']/steps")]
minutes = recipes.loc[recipes['id'] == int(recipe_id), 'minutes'].values[0]
author_id = recipes.loc[recipes['id'] == int(recipe_id), 'contributor_id'].values[0]

# Generating description
description = show_info(name, steps, minutes, author_id)

# Printing the description
print(description)
