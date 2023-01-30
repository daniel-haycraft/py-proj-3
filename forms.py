from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, SelectField, SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
   username = StringField('Username', [validators.InputRequired()])
   password = PasswordField('Password', [validators.InputRequired()])

choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

class QuantityForm(FlaskForm):
   choicy = SelectField(label='Quantity', choices = [(choice, choice) for choice in choices])
   submit = SubmitField(label='Submit')


