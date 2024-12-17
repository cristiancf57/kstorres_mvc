from flask import request,redirect,url_for,Blueprint
from datetime import datetime
from models.proyectos_model import Proyecto
from models.usuario_model import Usuario
from models.factura_model import Factura
from views import proyecto_view

proyecto_bp=Blueprint('proyecto',__name__,url_prefix='/proyectos')

@proyecto_bp.route('/')
def index():
    # recupera todo los registros de proyectos
    cont_p=Proyecto.query.count()
    cont_pryent=Proyecto.query.filter_by(estado = 'Entregado').count()
    porp= (cont_pryent * 100)/cont_p
    porp=round(porp,2)
    cont_usr = Usuario.query.count()
    cont_usup=Usuario.query.filter_by(id_rol = 3).count()
    porus=(cont_usup * 100)/cont_usr
    porus=round(porus,2)
    tsals = Factura.query.filter_by(deuda='cancelado').count()
    tot=Factura.query.count()
    pors = (tsals * 100)/tot
    porsl=round(pors,2)
    # estds=(cont_p,porp,cont_usr,porus,total_sal,porsl)
    proyectos= Proyecto.get_all()
    usuarios = Usuario.get_all()
    facturas = Factura.get_all()
    return proyecto_view.list(proyectos,usuarios,facturas,cont_p,porp,cont_usr,porus,tot,porsl)

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

    usuarios = Usuario.query.filter_by(id_rol=3)
    return proyecto_view.create(usuarios)

@proyecto_bp.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    proyects= Proyecto.get_by_id(id)
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
        id_usuario=request.form['id_usuario']

        fecha_inicio = datetime.strptime(fechafn_str,'%Y-%m-%d').date()
        fecha_fin = datetime.strptime(fechain_str,'%Y-%m-%d').date()

        # actualizar
        proyects.update(proyecto=proyecto,caracteristica=caracteristica,superfice=superficie,ubicacion=ubicacion,imagen=imagen,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,estado=estado,presupuesto=presupuesto,id_usuario=id_usuario)
        return redirect(url_for('proyecto.index'))
    
    usuarios=Usuario.query.filter_by(id_rol=3)
    return proyecto_view.edit(proyects,usuarios)

@proyecto_bp.route('/delete/<int:id>')
def delete(id):
    proyecto=Proyecto.get_by_id(id)
    proyecto.delete()
    return redirect(url_for('proyecto.index'))