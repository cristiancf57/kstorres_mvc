from flask import render_template

def inicio():
    return render_template('login/index.html')

def create(usuarios):
    return render_template('login/create.html',usuarios=usuarios)

def recuperar(user):
    render_template('login/recuperar',user=user)