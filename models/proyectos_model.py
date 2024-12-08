from database import db

class Proyecto(db.Model):
    __tablename__='proyectos'
    id = db.Column(db.Integer,primary_key=True)
    proyecto = db.Column(db.String(100),nullable=False)
    caracteristica = db.Column(db.String(100),nullable=False)
    superfice = db.Column(db.Numeric(15),nullable=True)
    ubicacion = db.Column(db.String(100),nullable=False)
    imagen = db.Column(db.String(200),nullable=True)
    fecha_inicio = db.Column(db.Date,nullable=False)
    fecha_fin = db.Column(db.Date,nullable=True)
    estado = db.Column(db.String(20),nullable=True)
    presupuesto = db.Column(db.Numeric(10,2),nullable=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuarios.id'),nullable=False)
    # gastos = db.relationship('Gastos',backref='gasto',lazy=True)
    # intentario = db.relationship('Inventarios',backref='almacen',lazy=True)
    # foto = db.relationship('Fotos',backref='foto',lazy=True)
    # especificar la relacion
    usuario = db.relationship('Usuario',backref='proyecto')

    def __init__(self,proyecto,caracteristica,superfice,ubicacion,imagen,fecha_inicio,fecha_fin,estado,presupuesto,id_usuario):
        self.proyecto = proyecto
        self.caracteristica = caracteristica
        self.superfice = superfice
        self.ubicacion = ubicacion
        self.imagen = imagen
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.presupuesto = presupuesto
        self.id_usuario = id_usuario
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Proyecto.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Proyecto.query.get(id)
    
    @staticmethod
    def get_rol():
        return Proyecto.query.filter_by(id_rol=2).all()
    
    def update(self,proyecto=None,caracteristica=None,superfice=None,ubicacion=None,imagen=None,fecha_inicio=None,fecha_fin=None,estado=None,presupuesto=None,id_usuario=None):
        if proyecto:
            self.proyecto=proyecto
        if caracteristica:
            self.caracteristica=caracteristica
        if superfice:
            self.superfice=superfice
        if ubicacion:
            self.ubicacion=ubicacion
        if imagen:
            self.imagen=imagen
        if fecha_inicio:
            self.fecha_inicio=fecha_inicio
        if fecha_fin:
            self.fecha_fin=fecha_fin
        if estado:
            self.estado=estado
        if presupuesto:
            self.presupuesto=presupuesto
        if id_usuario:
            self.id_usuario=id_usuario

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
