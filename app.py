from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("form.html")
@app.route('/submit',methods=['POST'])
def home():
    username=request.form.get("username")
    password=request.form.get("password")
    age=request.form.get("age")
    
    return render_template("greetings.html",username=username,age=age,password=password)
if __name__ == '__main__':
    app.run(debug=True)


    