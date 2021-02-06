from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)

##decorator
@main.route('/')
@main.route('/home')
def home():
    
    return ("<h1>Hello Flask</h1>")
