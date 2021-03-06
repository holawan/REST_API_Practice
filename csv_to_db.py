import csv
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mafrapjt.settings")
django.setup() 


from Maincategory.models import Recipe,Material,Procedure,Type,Nation

csv_path = 'C:/Users/SAMSUNG/Desktop/web_pjt/data/cleandata/type_name.csv'

with open(csv_path, newline='',encoding='utf-8') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			Type.objects.create(
				name = row['name'],
			)

csv_path = 'C:/Users/SAMSUNG/Desktop/web_pjt/data/cleandata/nation_name.csv'

with open(csv_path, newline='',encoding='utf-8') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			Nation.objects.create(
				name = row['name'],
			)

csv_path = 'C:/Users/SAMSUNG/Desktop/web_pjt/data/cleandata/recipe_basic.csv'

with open(csv_path, newline='',encoding='utf-8') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			Recipe.objects.create(
				# id= row['id'], 
                # ForeignKey의 경우 field명 뒤에 _id 입력
				# [Your-Field_1]_id   = row['[Your-Field_1]_id'], 
                # ForeignKey 외 field명 입력
				recipeName = row['recipeName'],
                summary = row['summary'],
                nation_id = row['nation_id'],
                type_id = row['type_id'],
                cookingTime = row['cookingTime'],
                calorie = row['calorie'],
                QNT = row['QNT'],
                level = row['level'],
                idrType = row['idrType'],
                image = row['image'],
			)
csv_path = 'C:/Users/SAMSUNG/Desktop/web_pjt/data/cleandata/recipe_material.csv'
with open(csv_path, newline='',encoding='utf-8') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
            # recipe_id = Recipe.objects.get(name=row['menu'])
			Material.objects.create(
				recipe_id = row['recipe_id'],
                irdnt_name = row['irdnt_name'],
                irdnt_cpcty = row['irdnt_cpcty'],
                irdnt_ty_nm = row['irdnt_ty_nm'],
			)
csv_path = 'C:/Users/SAMSUNG/Desktop/web_pjt/data/cleandata/recipe_procedure.csv'
with open(csv_path, newline='',encoding='utf-8') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			Procedure.objects.create(
				recipe_id = row['recipe_id'],
                order_id = row['order_id'],
                cooking_dc = row['cooking_dc'],
                step_img = row['step_img'],
                step_tip = row['step_tip'],
			)