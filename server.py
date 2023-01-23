from flask import Flask, render_template, redirect, flash, request
import jinja2
from melons import get_all
app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined  # for debugging purposes
@app.route('/')
def home():
   return render_template('base.html')

@app.route('/melons')
def show_all():
   return render_template('base.html', melons = get_all('melons.csv'))

if __name__ == "__main__":
   app.env = "development"
   app.run(debug = True, port = 8000, host = "localhost")
