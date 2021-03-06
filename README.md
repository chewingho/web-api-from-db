# web-api-from-db and dockerize
----	
## Description	
> 使用Flask將[博客來的爬蟲結果](https://github.com/chewingho/web-crawler-hot-item-of-books)  
  1.製作成Web API，並製作成Docker映像檔後執行容器  
  2.將Web API佈署到[Heroku](https://kateho-api.herokuapp.com/)  

## Process
1. 安裝所需套件([requirements.txt](https://github.com/chewingho/web-api-from-db/blob/master/requirements.txt))後，import要使用到的module
```python	
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
```
2. 設定資料庫連線
3. 透過ORM取得資料庫資料
4. 透過裝飾器@app.route()定義路由
> /all->資料庫所有分類的資料  
> /categories?category=中文書/簡體書/MOOK，顯示中文書/簡體書/MOOK分類下的資料
5. 執行python，啟動Web應用程式
6. 佈署到，取得WEB API
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```  
  ![首頁](https://github.com/chewingho/web-api-from-db/blob/master/readme%E5%9C%96%E7%89%87/homepage.PNG)  
  ![MOOK分類](https://github.com/chewingho/web-api-from-db/blob/master/readme%E5%9C%96%E7%89%87/MOOK%E5%88%86%E9%A1%9E.PNG)



## Dockerize  
1. 撰寫requirements.txt    
> 我是用Anaconda來管理套件，透過book.py import的套件與指令```conda list```來看有哪些套件要填到requirements.txt，但是還是有漏掉的例如因為我沒有import pymysql，所以剛開始沒有填，之後發現有錯誤才補上去。
```
Flask
flask_sqlalchemy
SQLAlchemy
pymysql
datetime
```
2. 撰寫Dockerfile 
> **FROM** 使用Python:3.7.4作為基底映像檔  
> **LABEL** 開發者的資訊  
> **WORKDIR** 設定預設目錄路徑，之後RUN、CMD皆會在/app這個路徑下執行  
> **ADD** 將本地端的檔案(requirements.txt、book.py)加到映像檔的指定路徑  
> **RUN** 執行建立映像檔時的指令或安裝，即執行指令```pip install -r requirements.txt```  
> **EXPOSE** 宣告在映像檔中預設要使用(對外)的連接埠 
> **CMD**  設定映像檔啟動為容器時要執行的指令，即執行指令```python book.py```  
```
FROM python:3.7.4
LABEL maintainer kateho
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python book.py
```  
3. 建立映像檔  
```
docker image build -t dockerfile_book .
```  
4. 啟動容器  
> 第一個5000為Linux VM(IP:192.168.99.100)的Port，第二個是容器的，也就是我們剛剛Dockerfile中的```EXPOSE 5000```  
```
docker run -p 5000:5000 dockerfile_book
```  
> 將IP改成Linux VM的192.168.99.100，因為我筆電作業系統是Windows 10沒有 Hyper V，是安裝Docker Toolbox來使用Docker  
![Docker Toolbox](https://github.com/chewingho/web-api-from-db/blob/docker/readme%E5%9C%96%E7%89%87/Docker%20Toolbox.png)  
![Docker IP](https://github.com/chewingho/web-api-from-db/blob/docker/readme%E5%9C%96%E7%89%87/Docker%20IP.PNG)  
> 另外，若要重新執行相同的docker run指令，因為Port 5000已經被剛剛啟動的容器使用，必須透過```docker ps```、```docker stop <Container ID>```來停止容器再執行
![docker run 失敗](https://github.com/chewingho/web-api-from-db/blob/docker/readme%E5%9C%96%E7%89%87/docker%20run%20%E5%A4%B1%E6%95%97.png)  

## Deploy on Heroku  
1. 申請免費雲端資料庫，並將資料匯入資料庫(當時只匯入單代資料(即某一週的爬蟲結果))  
2. 除了book.py，需再撰寫以下檔案：
> **Procfile** 
```
web gunicorn book:app
```
> **requirements.txt** 較Docker佈署多了gunicorn
> **runtime.txt** 
```
python-3.7.6
```
3. 透過Heroku Git佈署到Heroku
![heroku](https://github.com/chewingho/web-api-from-db/blob/master/readme%E5%9C%96%E7%89%87/heroku.PNG)  
4. 成功佈署，https://kateho-api.herokuapp.com/  
----
## Review ##  
  Web API只能在本地端顯示，因此學了如何將Web API佈署到Heroku。  
  也第一次使用Docker，記錄自己使用Docker的過程。  

----	
## Reference
[Flask實作_基礎_05_render_template](https://hackmd.io/@shaoeChen/HJkOuSagf?type=view)  
[Dockerfile指令](https://www.jinnsblog.com/2018/12/docker-dockerfile-guide.html)  

