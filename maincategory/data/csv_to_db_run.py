import csv
import os, sys
sys.path.append(os.pardir)
import django
from .models import recipeBasic


def csv_to_db(django_model):
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mafrapjt.settings")
	django.setup() 
	csv_path = '/WEB_PJT/maincategory/data/recipe_basic.csv'
	with open(csv_path, newline='') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			django_model.objects.create(
				id= row['id'], 
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
csv_to_db(recipeBasic)
   