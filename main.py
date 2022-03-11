from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # decorator
def start():
    return "<h1>My webpage is running.</h1>"

@app.route('/home')
def test():
    return "<h1>My Homepage.</h1>"

@app.route('/htmlpage')
def htmlpage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0") # host="127.0.0.1" local
