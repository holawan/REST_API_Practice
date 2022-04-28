import csv
import os, sys
import django

def csv_to_db(django_model):
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "[Your-Project].settings")
	django.setup() 
	csv_path = '/mafrapjt/maincategory/data/csv_to_db.csv'
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