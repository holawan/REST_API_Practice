# gonmo_api_Django


### 0426

- Django setting
  - secretkey 설정 
  - restful_api 설정
- 내일은 api 가져와서 DB적용하기. 

### 0427

- 회의 결과 
  - 백앤드는 express/ django로 일단 둘 다 개발해보기 
- 내 역할 : 메인 페이지 구축 위한 REST API 서버 만들기 

### 0428

- sqlite- > mysql
  - https://hongjuzzang.github.io/howto/mysql_django/
- 크롤링을 해서 데이터를 받은 후 DB에 그 때마다 데이터를 넣는다고 생각했는데 너무 비효율적이다 .
- 그냥 엑셀 받아서 전처리하고, 모델 깔끔히 만들어서 RESTAPI 넘겨주기로 함 
- image를 어떻게 넘겨줄지 고민해야함 
  - image가 파일 형태로 되어있는데 이걸 다 DB에 넣어야하나? 
  - http://file.okdab.com/recipe/148291443772500013.jpg
- 문제 발생 

  - 모델명을 RECIPE_BASIC으로 설정했는데,아래 형태로 형식이 맞지 않음, 언더바 제거를 고려 (해결)
  - ![admin](README.assets/admin.PNG)
  - 레시피 기본정보.csv  calorie 필드에 0kcal/null인 데이터가 있음, idrType(재료 종류)에도 null 존재 
    -  (null을 0칼로리로 조정? 홈페이지에서 세부 정보 찾아서 일일이 수정해야할 것 같음  )
    -  칼로리 2개, idrType 55개 null 존재 
    - 일단 model에 null=True옵션을 줘야 불러올 수 있을 것 같다. 
  - 
