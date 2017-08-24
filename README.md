# Blog_Project

Blog 使用 Django 1.9

功能包括 :

1. 文章的CRUD以及搜尋

2. 會員登錄系統

3. 文章評論串功能

前端格式參考了 bootstarp blog :

https://blackrockdigital.github.io/startbootstrap-blog-post/ 

## 前置設定

cd path/to/my/project

### 建立虛擬環境

virtualenv .

source bin/active

### 安裝套件

pip install -r requirements.txt

### 開始 Project

django-admin.py startproject Blog_Project


## 執行Django


### 模型與資料庫之同步

1. 建立migration資料檔，如果模型有任何異動，則會產生新的migration檔

python manage.py makemigrations

2. migrate會根據指定的migration記錄(利用編號指定)去將模型同步到資料庫

python manage.py migrate

### 創立 superuser

python manage.py createsuperuser

### 接著就可以跑看看了

python manage.py runserver
