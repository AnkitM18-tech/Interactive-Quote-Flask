from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
ENV = "dev"

if ENV == 'dev':
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://superuser:password@localhost/databasename'
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "ADD URL HERE"   #production url

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db =SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods=["POST"])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()