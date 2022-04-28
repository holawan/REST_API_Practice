import csv
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mafrapjt.settings")
django.setup() 


from Maincategory.models import recipeBasic

csv_path = 'C:/Users/SAMSUNG/Desktop/web_pjt/Maincategory/data/recipe_basic.csv'

with open(csv_path, newline='',encoding='utf-8') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			recipeBasic.objects.create(
				# id= row['id'], 
                # ForeignKey의 경우 field명 뒤에 _id 입력
				# [Your-Field_1]_id   = row['[Your-Field_1]_id'], 
                # ForeignKey 외 field명 입력
				recipeName = row['recipeName'],
                summary = row['summary'],
                nationName = row['nationName'],
                typeName = row['typeName'],
                cookingTime = row['cookingTime'],
                calorie = row['calorie'],
                QNT = row['QNT'],
                level = row['level'],
                idrType = row['idrType'],
                image = row['image'],

			)