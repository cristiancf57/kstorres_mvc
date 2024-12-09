from database import db

class Factura(db.Model):
    __tablename__='facturas'
    id = db.Column(db.Integer,primary_key=True)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyectos.id'),nullable=False)
    nro_factura= db.Column(db.Numeric(15),nullable=True)
    concepto = db.Column(db.String(250),nullable=True)
    monto = db.Column(db.Numeric(15,2),nullable=True)
    cuenta = db.Column(db.Numeric(15,2),nullable=True)
    saldo = db.Column(db.Numeric(15,2),nullable=True)
    deuda= db.Column(db.String(20),nullable=True)
    fecha = db.Column(db.Date,nullable=False)
    
    # Especificar relacion
    factura = db.relationship('Proyecto',backref='facturas')

    def __init__(self,id_proyecto,nro_factura,concepto,monto,cuenta,saldo,deuda,fecha):
        self.id_proyecto = id_proyecto
        self.nro_factura = nro_factura
        self.concepto = concepto
        self.monto = monto
        self.cuenta = cuenta
        self.saldo = saldo
        self.deuda = deuda
        self.fecha = fecha
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Factura.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Factura.query.get(id)
    
    def update(self,id_proyecto=None,nro_factura=None,concepto=None,cuenta=None,monto=None,saldo=None,deuda=None,fecha=None):
        if id_proyecto:
            self.id_proyecto=id_proyecto
        if nro_factura:
            self.nro_factura=nro_factura
        if concepto:
            self.concepto=concepto
        if cuenta:
            self.cuenta=cuenta
        if monto:
            self.monto=monto
        if saldo:
            self.saldo=saldo
        if deuda:
            self.deuda=deuda
        if fecha:
            self.fecha=fecha
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
