from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS= [
  {
    'id': 1,
    'title': "Data Analyst",
    'location': "Bengluru,India",
    'salary': 'Rs 12,00000'


  },
  {
    'id': 2,
    'title': "FrontEnd Developer",
    'location': "Delhi, India",
    'salary': 'Rs 15,00000'


  },
  {
    'id': 3,
    'title': "BackEnd Developer ",
    'location': "Pune, India",
    'salary': 'Rs 13,00000'


  },
  {
    'id': 4,
    'title': "Data Scientist",
    'location': "Hyderabad, India",
    'salary': 'Rs 12,00000'


  }

]

@app.route('/')

def hello_world():
  return render_template("home.html",jobs=JOBS, company_name="Harsh")




#Json End Point
#api route
@app.route('/api/jobs')

def list_job():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)