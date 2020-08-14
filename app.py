from flask import Flask,render_template,request,redirect,url_for
from flaskext.mysql import MySQL
import pymysql
mysql = MySQL()
app=Flask(__name__)
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='login_db '
app.config['MYSQL_DATABASE_HOST']='localhost'


@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET']) 
def login():
    conn=mysql.connect()
    cursor=conn.cursor(pymysql.cursor.Dictcursor)
    #outpu msg if something wrong
    msg=''
    #chekc if password and username exists in submitted form
    if request.method=='POST' and 'username' in request.form and 'password ' in request.form:
        username=request.form['username']
        password=request.form['password']
        #check if acount exist in mysql or in database
        cursor.execute('select * from  users where username=%s and password=%s',(username,password))
        user=cursor.fetchone()
        return redirect(url_for('profile'))

        if user:
            session['id']=user['id']
            session['username']=user['username']
            return redirect(url_for('profile'))
        else:
            msg="Incorrect username/password" 
    return render_template('login.html',msg=msg)

@app.route('/register',methods=['POST','GET'])
def register():
    return render_template('register.html')

@app.route('/profile',methods=['POST','GET'])
def profile():
    return render_template('profile.html')



if __name__=='__main__':
    app.run(debug=True)