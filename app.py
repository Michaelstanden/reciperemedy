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
 # Find all recipes in Mongo DB

    recipe = mongo.db.recipe.find().sort("_id", -1)

    # Pagination variable

    limit = 5

    # Find the requested page number (or default to page 1)

    page_number = int(request.args.get('page_number', 1))
    count = mongo.db.recipe.count_documents({})

    # identify how many recipe records to be skipped based on page number

    skip = (page_number - 1) * limit

    # skip relevant number of jobs

    recipe.skip(skip).limit(limit)

    # identify how many pages of results are needed

    pages = int(math.ceil(count / limit))

    # create a page range

    total_pages = range(1, pages + 1)
    return render_template(('recipe.html', page_number, total_pages, count)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')


@app.route('/lunch')
def lunch():
    return render_template('lunch.html')


@app.route('/dessert')
def dessert():
    return render_template('dessert.html')


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')


@app.route('/edit_recipe')
def edit_recipe():
    return render_template('edit_recipe.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)