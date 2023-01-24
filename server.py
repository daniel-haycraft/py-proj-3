import jinja2
from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
import melons
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'




app.jinja_env.undefined = jinja2.StrictUndefined  # for debugging purposes
@app.route('/')
def home():
   return render_template('base.html')

# @app.route('/melons')
# def all_melons():

#    return render_template('melons.html', melons = get_all('melons.csv'))
@app.route('/melons')
def all_melons():
   melon_list = melons.get_all_values()
   return render_template('all_melons.html', melon_list = melon_list)

@app.route('/melon/<melon_id>')
def melon_details(melon_id):
   
   return render_template('melon_details.html', melon = melons.get_by_id(melon_id))

@app.route('/add_to_cart/<melon_id>')
def add_to_cart(melon_id):
   return f"{melon_id} added to cart."

@app.route('/cart')
def cart():
   return render_template('cart.html', )

if __name__ == "__main__":
   app.env = "development"
   app.run(debug = True, port = 8000, host = "localhost")
