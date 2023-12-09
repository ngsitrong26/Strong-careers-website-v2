from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__) 

@app.route("/")
def hello_strong():
  jobs = load_jobs_from_db()
  return render_template('home.html',jobs=jobs,company_name='STrong')

@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)