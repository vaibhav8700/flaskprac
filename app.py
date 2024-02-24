# create a simple flask application


from flask import Flask,render_template,request,redirect,url_for


#create the flask app

app =Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello world</h1>"


@app.route('/welcome')
def welcome():
    return "WELCOME TO FLASK TUTORIAL"
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and the score is "+str(score)

@app.route('/calculate',methods = ['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        math = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])


        average = (math+science+history)/3
        result =''

        if average>=50:
            result = 'success'

        else:
            result = 'fail'

        #return redirect(url_for(result,score=average))


        return render_template('result.html',results = average)







if __name__=='__main__':

    app.run(debug=True)