from flask import render_template

def inicio():
    return render_template('welcome/index.html')

def nosotros(roles,profesion,usuarios):
    return render_template('welcome/nosotros.html',usuarios=usuarios,roles=roles,profesion=profesion)

def servicios():
    return render_template('welcome/servicios.html')

def proyectos():
    return render_template('welcome/proyectos.html')

def detall_proyect():
    return render_template('welcome/detalle.html')

def contacto():
    return render_template('welcome/contacto.html')