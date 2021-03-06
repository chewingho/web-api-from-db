from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# MySql datebase
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://python_user:python123@localhost/mynewdb"
app.config["JSON_AS_ASCII"] = False

db = SQLAlchemy(app)

# Class
class Book(db.Model):
    __tablename__ = 'tb_ranking'
    CATEGORY = db.Column(db.String(30), nullable=False)
    ITEM_NAME = db.Column(db.String(200),nullable=False,primary_key=True)
    RANKING = db.Column(db.Integer, nullable=False)
    HYPERLINK = db.Column(db.String(200), nullable=False)
    UPDATE_DATE = db.Column(db.DateTime, nullable=False,primary_key=True)

    def __init__(self, CATEGORY, ITEM_NAME, RANKING, HYPERLINK, UPDATE_DATE):
        self.CATEGORY = CATEGORY
        self.ITEM_NAME = ITEM_NAME
        self.RANKING = RANKING
        self.HYPERLINK = HYPERLINK
        self.UPDATE_DATE = UPDATE_DATE
book_list = []
books = Book.query.all()
row_dict = {}
for book in books:
    row_dict['category'] = book.CATEGORY
    row_dict['item_name'] = book.ITEM_NAME
    row_dict['ranking'] = book.RANKING
    row_dict['hyperlink'] = book.HYPERLINK
    row_dict['update_date'] = book.UPDATE_DATE.strftime("%Y/%m/%d")
    book_list.append(row_dict)
    row_dict = {}

# API 
@app.route('/')
def index():
    pagetitle = "HomePage"
    return render_template("index.html",
                            mytitle=pagetitle,
                            mycontent="Web api demo of Kateho")
    
@app.route('/categories', methods=['GET'])
def category():
    if 'category' in request.args:
        category = request.args['category']
    else:
        return jsonify(book_list)
    results = []

    for elem in book_list:
        if elem['category'] == category:
            results.append(elem)   
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)