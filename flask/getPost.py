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

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'HEY!!!!! {name}'
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)