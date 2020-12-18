from flask import Flask, render_template,request
from Data_Baseee.D_B import TestData
from Data_Baseee.class_Base_DB import DataBaseFile

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def login():
    alert = ""
    if request.method == 'POST':
        uname = request.form.get('username')
        pwd = request.form.get('password')
        if uname=='admin' and pwd=='pwd':
            return render_template('home.html')
        else:
            alert='Invalid Credential'
            return render_template('login.html', alert=alert)
    return render_template('login.html', alert=alert)

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')
        print(name, email, uname, pwd)

        data = TestData(name=name,email=email,uname=uname,pwd=pwd)
        con = db.get_connection()
        db.create_table(con,'new')
        db.insert_records(con,'new',data)
        db.close_connection(con)

        return render_template('login.html')
    return render_template('reg.html')

if __name__ == "__main__":
    db = DataBaseFile('Reggg.db')
    app.run(debug=True,port=5009)