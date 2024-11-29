from flask import request,redirect,url_for,Blueprint
from models.rol_model import Rol
from models.profesion_model import Profesion
from models.usuario_model import Usuario
from views import welcome_view

welcome_bp=Blueprint('inicio',__name__,url_prefix='/inicio')

@welcome_bp.route('/')
def index():
    return welcome_view.inicio()

@welcome_bp.route('/nosotros')
def nosotros():
    # recuperrar registros
    roles=Rol.get_all()
    profesion=Profesion.get_all()
    usuarios=Usuario.get_rol()
    return welcome_view.nosotros(roles,profesion,usuarios)

@welcome_bp.route('/servicios')
def servicios():
    return welcome_view.servicios()

@welcome_bp.route('/proyectos')
def proyectos():
    return welcome_view.proyectos()

@welcome_bp.route('/contacto')
def contacto():
    return welcome_view.contacto()