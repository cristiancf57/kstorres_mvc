from flask import request,redirect,url_for,Blueprint
from datetime import datetime
from models.proyectos_model import Proyecto
from models.inventario_model import Inventario
from models.factura_model import Factura
from views import inventario_view

inventario_bp=Blueprint('inventario',__name__,url_prefix='/inventarios')

@inventario_bp.route('/')
def index():
    # recupera todo los registros de inventarios
    inventarios = Inventario.query.all()
    projects =Proyecto.query.all()
    return inventario_view.list(inventarios,projects)

@inventario_bp.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        material=request.form['material']
        cantidad=request.form['cantidad']
        unidad=request.form['unidad']
        costounit=request.form['costo']
        totals = request.form['total']
        id_proyecto = request.form['id_proyecto']
        nro_factura = request.form['factura']

        if costounit and not totals:
            total=int(costounit) * int(cantidad)
            costo_unit=costounit

        if totals and not costounit:
            costo_unit = int(totals) / int(cantidad)
            total=totals

        if costounit and totals:
            if int(totals) == int(costounit)*int(cantidad):
                costo_unit=costounit
                total=totals
            else:
                total=int(costounit)*int(cantidad)
                costo_unit=costounit

        inventarios = Inventario(material,cantidad,unidad,costo_unit,total,id_proyecto)
        inventarios.save()

        concepto = material
        monto = total
        cuenta = 0
        saldo = total
        fecha = datetime.now().date()
        if saldo == 0:
            deuda = 'cancelado'

        if saldo == monto:
            deuda = 'nuevo'
        
        facturas = Factura(id_proyecto,nro_factura,concepto,monto,cuenta,saldo,deuda,fecha)
        facturas.save()

        return redirect(url_for('inventario.index'))

    projects = Proyecto.query.filter_by(estado ='En Construsccion')
    return inventario_view.create(projects)

@inventario_bp.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    inventario = Inventario.get_by_id(id)
    if request.method=='POST':
        material=request.form['material']
        cantidad=request.form['cantidad']
        unidad=request.form['unidad']
        costo_unit=request.form['costo']
        total = int(costo_unit) * int(cantidad)
        id_proyecto = request.form['id_proyecto']

        # actualizar
        inventario.update(material=material,cantidad=cantidad,unidad=unidad,costo_unit=costo_unit,total=total,id_proyecto=id_proyecto)
        return redirect(url_for('inventario.index'))
    
    projects = Proyecto.get_all()
    return inventario_view.edit(inventario,projects)

@inventario_bp.route('/delete/<int:id>')
def delete(id):
    inventario=Inventario.get_by_id(id)
    inventario.delete()
    return redirect(url_for('inventario.index'))