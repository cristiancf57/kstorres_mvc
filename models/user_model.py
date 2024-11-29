from database import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),nullable=False,unique=True)
    password = db.Column(db.Text,nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    # Relaciones
    user = db.relationship('Usuario',backref='users')

    def __init__(self,username,password,id_usuario):
        self.username = username
        self.password = self.hash_passwd(password)
        self.id_usuario = id_usuario

    @staticmethod
    def hash_passwd(password):
        return generate_password_hash(password)
    
    def verify_passwd(self,password):
        return check_password_hash(self.password,password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_username(username):
        return User.query.get(username)
    
    def update(self,username=None,password=None,id_usuario=None):
        if username:
            self.username=username
        if password:
            self.password=self.hash_passwd(password)
        if id_usuario:
            self.id_usuario=id_usuario

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
