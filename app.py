import os 
import flask_pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env 

SECRET_KEY = os.environ.get('MONGO_URI')
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Recipes'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipe.html", recipes=mongo.db.Recipes.find())


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)