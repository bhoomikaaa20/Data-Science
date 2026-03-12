from flask import Flask,render_template,request

'''
This is WSGI-which will send the requests from webserver to python application(data source)
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "hey!Welcome to flask"

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/result/<score>")
def result(score):
    return "result is "+ score


@app.route("/result2/<int:score>")
def result2(score):
    return "result2 is "+ str(score)


@app.route("/jinjaRes/<score>")
def jinjaRes(score):
    return render_template('jinja.html',scores=score)



if __name__=="__main__":
    app.run(debug=True)