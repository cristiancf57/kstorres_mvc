from flask import request,redirect,url_for,Blueprint,session,flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario_model import Usuario
from models.proyectos_model import Proyecto
from models.user_model import User
from views import login_view,proyecto_view

login_bp=Blueprint('login',__name__,url_prefix='/login')

@login_bp.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        
        user = User.query.filter_by(username=username).first()
        passw = User.query.filter_by(password=password).first()
        
        if user:
            session['user_id'] = user.id
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

