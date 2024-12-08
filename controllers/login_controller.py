from flask import request,redirect,url_for,Blueprint
from models.usuario_model import Usuario
from models.user_model import User
from views import login_view

login_bp=Blueprint('login',__name__,url_prefix='/login')

@login_bp.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=User.password(password)
        return redirect(url_for('proyectos.index'))
    return login_view.inicio()

@login_bp.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        id_usuario=request.form['id_usuario']

        user = User(username,password,id_usuario)
        user.save()
        return redirect(url_for('login.index'))

    return login_view.create()