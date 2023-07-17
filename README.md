# article_CRUD

**功能說明:**<br> 

有4支文章API，只有註冊並且登入的使用者(有JWT Access Token)才能夠進行CRUD操作。

**啟動說明:**

1. 安裝 Docker、Docker-compose、Docker Desktop、Python 3.7、Django 3.2、POSTMAN。Docker Desktop須保持開啟。
2. ```git clone https://github.com/vivian-wj-lin/article_CRUD.git```
3. ```pip install -r requirements.txt```
4. .env 檔案裡的 SECRET_KEY，需更換成實際在settings.py 的 SECRET_KEY
5. ```docker build -t myapp .```
6. ```docker-compose up```

**使用者註冊及登入API:**<br> 

PATCH: ```http://localhost:8000/api/register/```<br>
PATCH: ```http://localhost:8000/api/login/```<br>

**已經存在的使用者:**

```
{
"email": "icetea@gmail.com",
"password": "mypassword",
"username": "icetea@gmail.com"	
}
```

**4支文章API:**<br>

GET: ```http://localhost:8000/api/articles```<br>
POST: ```http://localhost:8000/api/articles/```<br>
DELETE: ```http://localhost:8000/api/articles/id/```<br>
PATCH: ```http://localhost:8000/api/articles/id/```<br>


**已經存在的一篇文章:**

```
{
  "title": "標題",
  "subtitle": "副標題",
  "title_image_url": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "date": "2023-07-16",
  "sum_title": "副標標題",
  "sum_description": "副標說明",
  "sum_image_url": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "sum_imageSource_description": "副標圖片來源說明",
  "sum_image_source_url": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "section_1_title": "段落1標題",
  "section_1_content": "段落1內文",
  "section_1_extended_reading_title": "段落1延伸閱讀標題",
  "section_1_extended_reading_link": "https://www.google.com/",
  "section_1_image": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "section_1_imageSource_description": "段落1圖片來源說明",
  "section_1_image_link": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "section_2_title": "段落2標題",
  "section_2_content": "段落2內文",
  "section_2_extended_reading_title": "段落2延伸閱讀標題",
  "section_2_extended_reading_link": "https://www.google.com/",
  "section_2_image": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "section_2_imageSource_description": "段落2圖片來源說明",
  "section_2_image_link": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "section_3_title": "段落3標題",
  "section_3_content": "段落3內文",
  "section_3_extended_reading_title": "段落3延伸閱讀標題",
  "section_3_extended_reading_link": "https://www.google.com/",
  "section_3_image": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672",
  "section_3_imageSource_description": "段落3圖片來源說明",
  "section_3_image_link": "https://msg-board-s3-bucket.s3.ap-northeast-1.amazonaws.com/msgboard/1677816640672"
}
```

**文章結構:**<br>

說明: 文章資料欄位與資料參考自 https://dailyview.tw/daily/2023/06/28<br>

文章結構:<br>
part 1: 標題圖片、標題、副標題、日期<br>
part 2: 副標標題、副標說明、副標圖片、副標圖片來源說明、副標圖片來源連結<br>
part 3: 段落、段落內文、段落延伸閱讀標題、段落延伸閱讀連結、段落圖片、段落圖片來源說明、段落圖片連結 *10個段落<br>

**pgAdmin**

```http://localhost:5050/browser/```<br>

登入帳密:<br>
| Email            | 密碼    |
| -------------- | --------- |
| icetea@gmail.com | admin     |

create a server 設定:<br>

| General        |                  |
| -------------- | ---------------- |
| Name           | anything you like|

| Connection     |                  |
| -------------- | ---------------- |
| Host Name      | db               |
| Port           | 5432             |
| Username       | mydatabaseuser   |
| Password       | mypassword       |

**查看 article table 和 user table的 Query String :**<br>
```select * from public. "article_article";```<br>
```select * from public. "auth_user";```<br>