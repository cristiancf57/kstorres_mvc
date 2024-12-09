from flask import request,redirect,url_for,Blueprint,session,flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario_model import Usuario
from models.proyectos_model import Proyecto
from models.user_model import User
from views import login_view,welcome_view,proyecto_view

login_bp=Blueprint('login',__name__,url_prefix='/login')

@login_bp.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        
        users = User.query.filter_by(username=username).first()
        if users and check_password_hash(users.password,password):
            idus=users.id_usuario
            # use_log=Usuario.query.filter_by(id=idus)
            use_log=Usuario.get_by_id(idus)
            nombre=use_log.nombre
            apellido=use_log.apellido
            profesion = use_log.profesions.profesion
            foto=use_log.foto
            session['user_log'] = ({'id':idus,'nombre':nombre,'apellido':apellido,'profesion':profesion,'foto':foto})
            return redirect('/proyectos/')
        else:
            flash("Usuario o contraseña incorrectos.")
            
    return login_view.inicio()

@login_bp.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        username=request.form['username']
        passwords=request.form['password']
        id_usuario=request.form['id_usuario']
        password=generate_password_hash(passwords)

        user = User(username,password,id_usuario)
        user.save()
        return  redirect('/proyectos/')
    usuuarios=Usuario.get_all()
    return login_view.create(usuuarios)

@login_bp.route('/vaciar',methods=['GET'])
def vaciar():
    # elimina de session user_log
    session.pop("user_log",None)
    return welcome_view.inicio()
