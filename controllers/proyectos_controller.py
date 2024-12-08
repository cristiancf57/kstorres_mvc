from flask import request,redirect,url_for,Blueprint
from datetime import datetime
from models.proyectos_model import Proyecto
from models.usuario_model import Usuario
from views import proyecto_view

proyecto_bp=Blueprint('proyecto',__name__,url_prefix='/proyectos')

@proyecto_bp.route('/')
def index():
    # recupera todo los registros de proyectos
    proyectos= Proyecto.get_all()
    usuarios = Usuario.get_all()
    return proyecto_view.list(proyectos,usuarios)

@proyecto_bp.route('/detalle')
def detalles():
    # recupera todo los registros de proyectos
    proyectos= Proyecto.get_all()
    return proyecto_view.detalles(proyectos)

@proyecto_bp.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        proyecto=request.form['proyecto']
        caracteristica=request.form['caracteristica']
        superficie=request.form['superficie']
        ubicacion=request.form['ubicacion']
        imagen=request.form['imagen']
        fechain_str=request.form['fecha_inicio']
        fechafn_str=request.form['fecha_fin']
        if fechafn_str:
            fechafin=fechafn_str
        else:
            fechafin=fechain_str
        estado=request.form['estado']
        presupuesto=request.form['presupuesto']
        id_usuario=request.form['id_usuario']

        fecha_inicio = datetime.strptime(fechain_str,'%Y-%m-%d').date()
        fecha_fin = datetime.strptime(fechafin,'%Y-%m-%d').date()

        proyectos = Proyecto(proyecto,caracteristica,superficie,ubicacion,imagen,fecha_inicio,fecha_fin,estado,presupuesto,id_usuario)
        proyectos.save()
        return redirect(url_for('proyecto.index'))

    usuarios = Usuario.get_all()
    return proyecto_view.create(usuarios)

@proyecto_bp.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    proyectos= Proyecto.get_by_id(id)
    if request.method=='POST':
        proyecto=request.form['proyecto']
        caracteristica=request.form['caracteristica']
        superficie=request.form['superficie']
        ubicacion=request.form['ubicacion']
        imagen=request.form['imagen']
        fechain_str=request.form['fecha_inicio']
        fechafn_str=request.form['fecha_fin']
        estado=request.form['estado']
        presupuesto=request.form['presupuesto']
        id_isuario=request.form['id_isuario']

        fecha_inicio = datetime.strptime(fechafn_str,'%Y-%m-%d').date()
        fecha_fin = datetime.strptime(fechain_str,'%Y-%m-%d').date()

        # actualizar
        proyectos.update(proyecto=proyecto,caracteristica=caracteristica,superficie=superficie,ubicacion=ubicacion,imagen=imagen,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,estado=estado,presupuesto=presupuesto,id_isuario=id_isuario)
        return redirect(url_for('proyecto.index'))
    
    usuarios=Usuario.query.all()
    return proyecto_view.edit(proyectos,usuarios)

@proyecto_bp.route('/delete/<int:id>')
def delete(id):
    proyecto=Proyecto.get_by_id(id)
    proyecto.delete()
    return redirect(url_for('proyecto.index'))