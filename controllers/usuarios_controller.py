from flask import request,redirect,url_for,Blueprint,session
from datetime import datetime
from models.usuario_model import Usuario
from models.profesion_model import Profesion
from models.rol_model import Rol
from views import usuario_view
from functools import wraps

usuario_bp=Blueprint('usuario',__name__,url_prefix='/usuarios')

@usuario_bp.route('/')
def index():
    # recupera todo los registros de usuarios
    usuarios = Usuario.query.all()
    profesions =Profesion.query.all()
    return usuario_view.list(usuarios,profesions)

@usuario_bp.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        foto_f=request.form['foto']
        if foto_f:
            foto=foto_f
        else:
            foto='defaul.jpg'
        telefono=request.form['telefono']
        salario=request.form['salario']
        obs='s/n'
        id_profesion=request.form['profesion_id']
        id_rol = 5

        usuarios = Usuario(nombre,apellido,foto,telefono,salario,obs,id_profesion,id_rol)
        usuarios.save()
        return redirect(url_for('usuario.index'))

    profesiones = Profesion.get_all()
    return usuario_view.create(profesiones)

@usuario_bp.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    usuario= Usuario.get_by_id(id)
    if request.method=='POST':
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        foto=request.form['foto']
        telefono=request.form['telefono']
        salario=request.form['salario']
        obs=request.form['obs']
        id_profesion=request.form['id_profesion']
        id_rol=request.form['id_rol']

        # actualizar
        usuario.update(nombre=nombre,apellido=apellido,foto=foto,telefono=telefono,salario=salario,obs=obs,id_profesion=id_profesion,id_rol=id_rol)
        return redirect(url_for('usuario.index'))
    
    profesiones = Profesion.get_all()
    roles = Rol.get_all()
    return usuario_view.edit(usuario,profesiones,roles)

@usuario_bp.route('/delete/<int:id>')
def delete(id):
    usuario=Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))