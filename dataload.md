# Data Load 후 서버 켜는 방법

1. 메인 폴더에서 Python 파일 열기

2. 가상환경 생성

   - python -m venv venv

3. 가상환경 접속

   ```
   source venv/script/activate
   ```

4. requiremetns.txt 다운 

   ```
   pip install -r requirements.txt
   ```

5. sqlite에 데이터 로드하기

   ```
   python manage.py migrate
   ```

   ```python
   python manage.py loaddata material.json nation.json procedure.json recipe.json
   ```

5. superuser 만들기

   ```python
   python manage.py createsuperuser
   ```

6. 서버 켜기 

```python
python manage.py runserver
```

#### 현재 url은 api/v1이며, 스웨거 접속은 superuser만든 후 메인 주소/admin으로 들어가서 로그인 하시면 테스트 하실 수 있습니다!
