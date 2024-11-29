from database import db

class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    foto = db.Column(db.Text,nullable=True)
    telefono = db.Column(db.Numeric(9),nullable=True)
    salario = db.Column(db.Numeric(10,2),nullable=False)
    obs = db.Column(db.Text,nullable=True)
    id_profesion = db.Column(db.Integer,db.ForeignKey('profesiones.id'),nullable=False)
    id_rol = db.Column(db.Integer,db.ForeignKey('roles.id'),nullable=False)
    # especificar la relacion
    rol = db.relationship('Rol', backref='usuarios')
    profesion = db.relationship('Profesion',backref='usuarios')

    def __init__(self,nombre,apellido,foto,telefono,salario,obs,id_profesion,id_rol):
        self.nombre = nombre
        self.apellido = apellido
        self.foto = foto
        self.telefono = telefono
        self.salario = salario
        self.obs = obs
        self.id_profesion = id_profesion
        self.id_rol = id_rol
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    @staticmethod
    def get_rol():
        return Usuario.query.filter_by(id_rol=2).all()
    
    def update(self,nombre=None,apellido=None,foto=None,telefono=None,salario=None,obs=None,id_profesion=None,id_rol=None):
        if nombre:
            self.nombre=nombre
        if apellido:
            self.apellido=apellido
        if foto:
            self.foto=foto
        if telefono:
            self.telefono=telefono
        if salario:
            self.salario=salario
        if obs:
            self.obs=obs
        if id_profesion:
            self.id_profesion=id_profesion
        if id_rol:
            self.id_rol=id_rol

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
