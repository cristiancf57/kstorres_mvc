from flask import render_template

def list(usuarios,profesion):
    return render_template('usuarios/index.html',usuarios=usuarios,profesion=profesion)

def create(profesiones):
    # se requiere profesiones
    return render_template('usuarios/create.html',profesiones=profesiones)

def edit(usuario,profesiones,roles):
    # se requiere profesiones y usuarios
    return render_template('usuarios/edit.html',usuario=usuario,profesiones=profesiones,roles=roles)

def user_profile(usuario,profesiones,roles):
    return render_template('usuarios/user_profile.html',usuario=usuario,profesiones=profesiones,roles=roles)