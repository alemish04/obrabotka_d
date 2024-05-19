import pandas as pd
import random
import xlwings as xw

# 1. Load data from reviews_sample.csv and recipes_sample.csv
reviews_df = pd.read_csv('reviews_sample.csv', index_col=0)
recipes_df = pd.read_csv('recipes_sample.csv', usecols=['id', 'name', 'minutes', 'submitted', 'description', 'n_ingredients'])

# 2. Randomly select 5% of rows from each table
reviews_sample = reviews_df.sample(frac=0.05, random_state=1)
recipes_sample = recipes_df.sample(frac=0.05, random_state=1)

# Save to Excel file
with pd.ExcelWriter('recipes.xlsx') as writer:
    recipes_sample.to_excel(writer, sheet_name='Рецепты', index=False)
    reviews_sample.to_excel(writer, sheet_name='Отзывы', index=False)

# 3. Add a column `seconds_assign` to the `Рецепты` sheet
app = xw.App(visible=False)
wb = app.books.open('recipes.xlsx')
sheet = wb.sheets['Рецепты']
minutes = sheet.range('C2:C' + str(sheet.range('A' + str(sheet.cells.last_cell.row)).end('up').row)).value
seconds_assign = [minute * 60 for minute in minutes]
sheet.range('G1').value = 'seconds_assign'
sheet.range('G2').options(transpose=True).value = seconds_assign

# 4. Add a column `seconds_formula` to the `Рецепты` sheet using Excel formulas
sheet.range('H1').value = 'seconds_formula'
sheet.range('H2:H' + str(len(minutes) + 1)).formula = '=C2*60'

# 5. Make titles of added columns bold and center aligned
sheet.range('G1:H1').api.Font.Bold = True
sheet.range('G1:H1').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter

# 6. Color cells in the `minutes` column
for i in range(2, len(minutes) + 2):
    cell = sheet.range('C' + str(i))
    if cell.value < 5:
        cell.color = (0, 255, 0)  # green
    elif 5 <= cell.value < 10:
        cell.color = (255, 255, 0)  # yellow
    else:
        cell.color = (255, 0, 0)  # red

# 7. Add a column `n_reviews` with the count of reviews for each recipe
sheet_reviews = wb.sheets['Отзывы']
recipe_ids = [id for id in sheet.range('A2:A' + str(sheet.range('A' + str(sheet.cells.last_cell.row)).end('up').row)).value]
reviews_count = [reviews_sample[reviews_sample['recipe_id'] == id].shape[0] for id in recipe_ids]
sheet.range('I1').value = 'n_reviews'
sheet.range('I2').options(transpose=True).value = reviews_count

# Save and close the workbook
wb.save()
wb.close()
app.quit()
