import jinja2
from flask import Flask, render_template, url_for, redirect, session, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired

from forms import LoginForm, QuantityForm
import melons
import customers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

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
   qform = QuantityForm()


   if 'cart' not in session:
      session['cart'] = {}

   if 'username' not in session:
      flash('you must login first')
      return redirect('/login')

   cart = session['cart']
   session.modified = True
   cart[melon_id]= cart.get(melon_id, 0) + 1
   flash(f"{melon_id} added to cart.")
   return redirect('/cart')


@app.route('/cart', methods = ["GET", 'POST'])
def cart():
   qform = QuantityForm()
   
   order_total = 0
   cart_melons = []
   cart = session.get("cart", {})
   if 'username' not in session:
      flash('you must login first')
      return redirect('/login')
   
   
   for melon_id, initial in cart.items():

      melon = melons.get_by_id(melon_id)

      
      initial += int(qform.choicy.data or 0)
      
      total_price = initial* melon.price

      order_total += total_price

      melon.total_price = total_price
      initial + int(qform.choicy.data or 0)
      melon.initial = initial
      cart_melons.append(melon)
      

   return render_template('cart.html', cart_melons = cart_melons,  qform = qform, order_total = order_total)
         



@app.route("/empty-cart")
def empty_cart():
   session["cart"] = {}
   return redirect('/cart')
   
@app.route('/login', methods =['GET', 'POST'])
def login():
   form = LoginForm(request.form)
   if form.validate_on_submit():
      print(form.username.data)
      username = form.username.data
      password = form.password.data

      user = customers.get_by_username(username)

      if not user or user['password'] != password:
         flash('incorrect username or password please try again')
         return redirect('/login')
      flash('Logged In.')
      session["username"] = user['username']
      return redirect('/melons')
   return render_template("login.html", form = form)

@app.route('/logout')
def logout():
   del session["username"]
   flash('logged out')
   return redirect('/login')

@app.errorhandler(404)
def error(e):
   return render_template('lol.html',)

if __name__ == "__main__":
   app.run(debug = True, port = 8000, host = "localhost")
