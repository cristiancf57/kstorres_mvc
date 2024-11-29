from database import db

class Profesion(db.Model):
    __tablename__='profesiones'
    id = db.Column(db.Integer, primary_key=True)
    profesion = db.Column(db.String(60),nullable=False)
    abreviado = db.Column(db.String(5),nullable=False)
    # Relacion con ventas

    def __init__(self,profesion,abreviado):
        self.profesion = profesion
        self.abreviado = abreviado
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Profesion.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Profesion.query.get(id)
    
    def update(self,profesion=None,abreviado=None):
        if profesion and abreviado:
            self.profesion=profesion
            self.abreviado=abreviado
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()