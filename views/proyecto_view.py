from flask import render_template

def list(proyectos,usuarios):
    return render_template('proyectos/index.html',proyectos=proyectos,usuarios=usuarios)

def create(usuarios):
    # se requiere productos y usuarios
    return render_template('proyectos/create.html',usuarios=usuarios)

def edit(proyectos,usuarios):
    # se requiere proyectos y usuarios
    return render_template('proyectos/edit.html',proyectos=proyectos,usuarios=usuarios)

def detalles(proyectos):
    # se requiere proyectos
    return render_template('proyectos/detalles.html',proyectos=proyectos)