from flask import render_template

def inicio():
    return render_template('login/index.html')

def create():
    return render_template('login/create')

def recuperar(user):
    render_template('login/recuperar',user=user)