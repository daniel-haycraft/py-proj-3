from flask import Flask, render_template, redirect, flash, request
import jinja2

app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined  # for debugging purposes

if __name__ == "__main__":
   app.env = "development"
   app.run(debug = True, port = 8000, host = "localhost")