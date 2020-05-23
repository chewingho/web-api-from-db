# web-api-from-db
----	
## Description	
> 使用Flask將[將博客來的爬蟲結果](https://github.com/chewingho/web-crawler-hot-item-of-books)製作成Web API

## Process
1. import要使用到的module
```python	
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
```
2. 設定資料庫連線
3. 透過ORM取得資料庫資料
4. 透過裝飾器@app.route()定義路由
> /all->資料庫所有分類的資料  
> /categories?category=中文書/簡體書/MOOK，顯示中文書/簡體書/MOOK分類下的資料
5. 執行python，啟動Web應用程式

----
## Review ##  
  Web API只能在localhost顯示，因此學了如何將Web API佈署到Heroku  

----	
## Reference
[Flask實作_基礎_05_render_template](https://hackmd.io/@shaoeChen/HJkOuSagf?type=view)
