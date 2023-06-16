
from flask import Flask,render_template,redirect,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:root@localhost:5432/ToDoApp"
db=SQLAlchemy(app)

#migrate = Migrate(app, db)

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(100),nullable=False)

with app.app_context():
    db.create_all()

@app.route('/home',methods=['POST','GET'])
def home():  # put application's code here
    # num_rows_updated = Users.query.filter_by(id=21).update(dict(content='my_new_email@example.com'))
    # db.session.commit()
    if request.method=='POST':
        name=request.form['content']
        user=Users(content=name)
        db.session.add(user)
        db.session.commit()
    users = Users.query.filter_by()
    return render_template('home.html',todo_list=users)

@app.route('/remove',methods=['POST'])
def remove():
    id=request.form['id']
    obj = Users.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    return redirect('/home')\

@app.route('/update',methods=['POST'])
def update():
    id=request.form['id']
    content=request.form['content']
    result = Users.query.filter_by(id=id).update(dict(content=content))
    db.session.commit()
    return redirect('/home')
if __name__ == '__main__':
    app.run()
