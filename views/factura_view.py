from flask import render_template

def list(facturas,projects):
    return render_template('facturas/index.html',facturas=facturas,projects=projects)

def create(projects):
    # se requiere projects
    return render_template('facturas/create.html',projects=projects)

def edit(factura,projects):
    # se requiere factura y proyectos
    return render_template('facturas/edit.html',factura=factura,projects=projects)
