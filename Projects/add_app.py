from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('add1.html')
@app.route('/add', methods=['POST','GET'])
def add1():
    num1=request.form['first']
    num2=request.form['second']
    rslt = (int(num1) + int(num2))
    print(num1, num2, rslt)
    # return render_template('add2.html', result1=rslt)
    return render_template('add1.html', result=rslt)


if __name__ == "__main__":
    app.run(debug=True)