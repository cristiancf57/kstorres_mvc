from database import db

class Rol(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key=True)
    cargo = db.Column(db.String(50),nullable=False)
    # Relacion con ventas

    def __init__(self,cargo):
        self.cargo = cargo
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Rol.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Rol.query.get(id)
    
    def update(self,cargo=None):
        if cargo:
            self.cargo=cargo
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()