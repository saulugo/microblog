from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Saul'} #fake user
	posts = [ #fake array of posts
		{
			'author': {'nickname':'John'},
			'body': 'Beautiful day in Madrid'
		},
		{
			'author': {'nickname':'Carlos'},
			'body': 'I like the food here'
		}
	]
	return render_template('index.html',
							title='Home',
							user=user,
							posts=posts)
							
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
							title='Sign In',
							form=form)
							