from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return "Hellow world! this is root"

@app.route("/template_test")
def tepmplate_test():
    return render_template("index.html", name="Rabb")

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<user>')
def name(user):
  return "Hi " + user

@app.route('/repeat/<times>/<converter>')
def convert(times, converter):
  return int(times) * converter


if __name__=="__main__":  
    app.run(debug=True)