from flask import Flask,render_template,redirect,url_for

'''
This is WSGI-which will send the requests from webserver to python application(data source)
'''

app=Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for('about'))

@app.route("/about")
def about():
    return render_template('about.html')



if __name__=="__main__":
    app.run(debug=True)