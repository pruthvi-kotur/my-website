from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def home():
  return render_template("home.html")

@app.route('/aboutme')
def aboutme():
  return render_template("aboutme.html")

@app.route('/education')
def education():
  return render_template("education.html")

@app.route('/skills')
def skills():
  return render_template("skills.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)