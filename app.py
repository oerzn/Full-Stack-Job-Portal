from flask import Flask, render_template, jsonify
from database import load_jobs_with_db, load_job_with_db

app = Flask(__name__)

# JOBS= [
#   {
#     'id': 1,
#     'title': "Data Analyst",
#     'location': "Bengluru,India",
#     'salary': 'Rs 12,00000'


#   },
#   {
#     'id': 2,
#     'title': "FrontEnd Developer",
#     'location': "Delhi, India",
#     'salary': 'Rs 15,00000'


#   },
#   {
#     'id': 3,
#     'title': "BackEnd Developer ",
#     'location': "Pune, India",
#     'salary': 'Rs 13,00000'


#   },
#   {
#     'id': 4,
#     'title': "Data Scientist",
#     'location': "Hyderabad, India",
#     'salary': 'Rs 12,00000'


#   }

# ]

@app.route('/')

def hello_job_portal():
  jobs_list = load_jobs_with_db()
  return render_template("home.html",jobs=jobs_list, company_name="Harsh")




#Json End Point
#api route
@app.route('/api/jobs')

def list_job():
  jobs_list = load_jobs_with_db()
  return jsonify(jobs_list)

@app.route("/jobs/<id>")
def show_job(id):
  job = load_job_with_db(id)
  if job == None:
    return "Job Not found, 404", 404
  return render_template("jobpage.html", job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)