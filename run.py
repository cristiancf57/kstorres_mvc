from flask import Flask,redirect,request,session
from controllers import welcome_controller
from controllers import login_controller
from controllers import proyectos_controller
from controllers import usuarios_controller
from controllers import inventarios_controller
from controllers import facturas_controller
from database import db
from functools import wraps

app=Flask(__name__)
app.secret_key = 'clavesecreta'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/kstorres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(welcome_controller.welcome_bp)
app.register_blueprint(login_controller.login_bp)
app.register_blueprint(proyectos_controller.proyecto_bp)
app.register_blueprint(usuarios_controller.usuario_bp)
app.register_blueprint(inventarios_controller.inventario_bp)
app.register_blueprint(facturas_controller.factura_bp)

@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return(dict(is_active=is_active))

@app.route('/')
def home():
    return redirect('/inicio')
    
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)