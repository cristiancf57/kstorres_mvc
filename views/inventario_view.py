from flask import render_template

def list(inventarios,projects):
    return render_template('inventarios/index.html',inventarios=inventarios,projects=projects)

def create(projects):
    # se requiere projects
    return render_template('inventarios/create.html',projects=projects)

def edit(inventario,projects):
    # se requiere inventario y proyectos
    return render_template('inventarios/edit.html',inventario=inventario,projects=projects)
