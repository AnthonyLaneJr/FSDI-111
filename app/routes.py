from flask import Flask     #from flask module imports the flask class

app = Flask(__name__)         # create an instance of the Flask class into the app
                            #app is now an object
@app.get("/")               # flask decoraor that allows us to map a route to a view function
def index():                #our view function 
    return "<h1>Hello, world!</h1>" #return statement


@app.get("/about")
def get_about():
    me ={
        "first_name": "Anthony",
        "last_name": "Lane",
        "hobbies": "Working out",
        "active": True
    }
    return me