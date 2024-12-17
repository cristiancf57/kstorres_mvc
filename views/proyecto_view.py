from flask import render_template

def list(proyectos,usuarios,facturas,cont_p,porp,cont_usr,porus,total_sal,porsl):
    return render_template('proyectos/index.html',proyectos=proyectos,usuarios=usuarios,facturas=facturas,cont_p=cont_p,porp=porp,cont_usr=cont_usr,porus=porus,total_sal=total_sal,porsl=porsl)

def create(usuarios):
    # se requiere productos y usuarios
    return render_template('proyectos/create.html',usuarios=usuarios)

def edit(proyects,usuarios):
    # se requiere proyectos y usuarios
    return render_template('proyectos/edit.html',proyects=proyects,usuarios=usuarios)

def detalles(proyectos):
    # se requiere proyectos
    return render_template('proyectos/detalles.html',proyectos=proyectos)