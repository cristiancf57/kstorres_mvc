from flask import request,redirect,url_for,Blueprint
from datetime import datetime
from models.proyectos_model import Proyecto
from models.factura_model import Factura
from views import factura_view
from decimal import Decimal

factura_bp=Blueprint('factura',__name__,url_prefix='/facturas')

@factura_bp.route('/')
def index():
    # recupera todo los registros de facturas
    facturas = Factura.query.all()
    projects =Proyecto.query.all()
    return factura_view.list(facturas,projects)

@factura_bp.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        id_proyecto=request.form['id_proyecto']
        nro_factura=request.form['nro_factura']
        concepto=request.form['concepto']
        monto=request.form['monto']
        cuenta=request.form['cuenta']
        saldo=int(monto)-int(cuenta)
        fecha = datetime.now().date()
        
        if saldo == 0:
            deuda = 'cancelado'

        if saldo == int(monto):
            deuda = 'nuevo'

        if saldo >0 and saldo < int(monto):
            deuda= 'saldo'
        
        facturas = Factura(id_proyecto=id_proyecto,nro_factura=nro_factura,concepto=concepto,monto=monto,cuenta=cuenta,saldo=saldo,deuda=deuda,fecha=fecha)
        facturas.save()
        return redirect(url_for('factura.index'))

    projects = Proyecto.query.all()
    return factura_view.create(projects)

@factura_bp.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    factura = Factura.get_by_id(id)
    if request.method=='POST':
        id_proyecto=request.form['id_proyecto']
        nro_factura=request.form['nro_factura']
        concepto=request.form['concepto']
        saldop=request.form['saldo']
        monto =factura.monto
        cuenta=monto
        saldo='0.0'
        fecha = datetime.now().date()
        deuda = 'cancelado'
        # actualizar
        factura.update(id_proyecto=id_proyecto,nro_factura=nro_factura,concepto=concepto,monto=monto,cuenta=cuenta,saldo=saldo,deuda=deuda,fecha=fecha)
        return redirect(url_for('factura.index'))
    
    projects = Proyecto.get_all()
    return factura_view.edit(factura,projects)

@factura_bp.route('/delete/<int:id>')
def delete(id):
    factura=factura.get_by_id(id)
    factura.delete()
    return redirect(url_for('factura.index'))