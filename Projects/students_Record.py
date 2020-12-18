from flask import Flask,render_template, request
from stud_data.D_B import TestData
from stud_data.class_Base_DB import DataBaseFile


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def students_rec():
    if request.method == 'POST':
        name = request.form.get('name')
        cls = request.form.get('cls')
        mark = request.form.get('mark')
        grade = request.form.get('grade')
        print(name,cls,mark,grade)

        data = TestData(name=name,cls=cls,mark=mark,grade=grade)
        con = db.get_connection()
        db.create_table(con, 'stud_data')
        db.insert_records(con, 'stud_data', data)
        db.close_connection(con)
        return render_template('stud_recrd.html')
    return render_template('stud_recrd.html')


if __name__ == "__main__":
    db = DataBaseFile('student.db')
    app.run(debug=True)