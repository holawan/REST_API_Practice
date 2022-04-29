from django.db import models

# Create your models here.

class Recipe(models.Model) :
    #레시피 이름 
    recipeName = models.CharField(max_length = 30)
    #설명 
    summary = models.TextField()
    #국가 분류 (?) 한식/양식/중식 
    nationName = models.CharField(max_length= 30)
    #요리 분류 (밥/떡/국/만두/면 등 )
    typeName = models.CharField(max_length = 30)
    #조리시간 
    cookingTime = models.IntegerField()
    #칼로리 
    calorie = models.IntegerField()
    #인분 
    QNT = models.IntegerField()
    #조리 레벨 
    level = models.CharField(max_length=10)
    #재료 종류 ? 
    idrType = models.CharField(max_length = 20,null=True)
    #이미지
    image = models.TextField()


class Material(models.Model)  :
    #레시피 참조 
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    #재료명 
    irdnt_name= models.CharField(max_length=20)
    #재료 용량 
    irdnt_cpcty = models.CharField(max_length=10)
    #재료 타입
    irdnt_ty_nm = models.CharField(max_length=20)

class Procedure(models.Model) :
    #레시피 참조    
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    #조리순서
    order_id = models.IntegerField()
    #조리방법 
    cooking_dc = models.TextField()
    #스텝별 사진
    step_img = models.TextField(null=True)
    #스텝별 팁 
    step_tip = models.TextField()
