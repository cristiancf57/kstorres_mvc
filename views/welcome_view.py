from flask import render_template

def inicio():
    return render_template('welcome/index.html')

def nosotros(roles,profesion,usuarios):
    return render_template('welcome/nosotros.html',usuarios=usuarios,roles=roles,profesion=profesion)

def servicios(proyectos):
    return render_template('welcome/servicios.html',proyectos=proyectos)

def proyectos(proyectos,usuarios,profession):
    return render_template('welcome/proyectos.html',proyectos=proyectos,usuarios=usuarios,profession=profession)

def detall_proyect():
    return render_template('welcome/detalle.html')

def contacto():
    return render_template('welcome/contacto.html')