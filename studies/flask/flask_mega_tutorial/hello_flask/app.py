#!/usr/bin/env python
from flask import Flask, render_template, flash, redirect
from endpoints.calls import get_external_ip
from forms import LoginForm
import configargparse

parser = configargparse.get_argument_parser(name='default')
parser.add_argument('--secret-key', type=str, env_var='SECRET_KEY',
                    default='you-will-never-guess', help='secret key for secret stuff')


cfg = parser.parse_known_args()[0]

app = Flask(__name__)
app.config['SECRET_KEY'] = cfg.secret_key

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sam'}
    title = ''

    posts = [
        {
            'author': 'Bob',
            'body': 'this is a post'
         },
        {
            'author': 'Pete',
            'body': 'this is another post'
        },
    ]

    return render_template('index.html', user=user, title=title, posts=posts)


@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html', title=title)


@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('contact.html', title=title)


@app.route('/network')
def network():
    title = 'Network'
    ip = get_external_ip()

    return render_template('network.html', title=title, ip=ip)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user: {form.username.data} | remember_me: {form.remember_me.data}')
        return redirect('/index')

    title = 'Login'
    return render_template('login.html', title=title, form=form)



