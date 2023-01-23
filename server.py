from flask import Flask, render_template, redirect, flash, request
import jinja2
from melons import get_all, get_by_id
app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined  # for debugging purposes
@app.route('/')
def home():
   return render_template('base.html')

@app.route('/melons')
def show_all():
   return render_template('melons.html', melons = get_all('melons.csv'))

@app.route('/melon/<melon_id>')
def melon_details(melon_id):
   return render_template('id.html', mels = get_by_id(melon_id))

@app.route('/add_to_cart/<melon_id>')
def add_to_cart(melon_id):
   return f"{melon_id} added to cart."

@app.route('/cart')
def cart():
   render_template('cart.html', )

if __name__ == "__main__":
   app.env = "development"
   app.run(debug = True, port = 8000, host = "localhost")
