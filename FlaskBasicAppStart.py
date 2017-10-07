from flask import Flask, render_template

####################
# More info about the setup for Flask and React and what this does is at:
# https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9
####################
app = Flask(__name__, static_folder="./static/dist", template_folder="./static")


@app.route('/')
def hello_world():
    #return render_template("index.html")
    return "Hello World"

if __name__ == '__main__':
    app.run()
