from flask import Flask,redirect
from controllers import welcome_controller
from database import db

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/kstorres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(welcome_controller.welcome_bp)

@app.route('/')
def home():
    return redirect('/inicio')
    
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)