from database import db

class Inventario(db.Model):
    __tablename__='inventarios'
    id = db.Column(db.Integer,primary_key=True)
    material = db.Column(db.String(200),nullable=True)
    cantidad = db.Column(db.Numeric(10),nullable=False)
    unidad = db.Column(db.String(20),nullable=True)
    costo_unit = db.Column(db.Numeric(10,2),nullable=True)
    total = db.Column(db.Numeric(15,2),nullable=True)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyectos.id'),nullable=False)
    # Especificar relacion
    inventory = db.relationship('Proyecto',backref='inventarios')

    def __init__(self,material,cantidad,unidad,costo_unit,total,id_proyecto):
        self.material = material
        self.cantidad = cantidad
        self.unidad = unidad
        self.costo_unit = costo_unit
        self.total = total
        self.id_proyecto = id_proyecto
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Inventario.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Inventario.query.get(id)
    
    def update(self,material=None,cantidad=None,unidad=None,costo_unit=None,total=None,id_proyecto=None):
        if material:
            self.material=material
        if cantidad:
            self.cantidad=cantidad
        if unidad:
            self.unidad=unidad
        if costo_unit:
            self.costo_unit=costo_unit
        if total:
            self.total=total
        if id_proyecto:
            self.id_proyecto=id_proyecto

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
