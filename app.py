from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title': 'student',
    'location': 'Nghệ An',
    'salary':'VND. 1,000,000'
  },
  {
    'id':2,
    'title': 'back-end engineer',
    'location': 'Hà Nội',
    'salary':'VND. 15,500,000'
  },
  {
    'id':3,
    'title': 'front-end engineer',
    'location': 'Hồ Chí Minh',
    'salary':'VND. 12,000,000'
  },
  {
    'id':4,
    'title': 'AI',
    'location': 'Singapore',
    'salary':'$. 30,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='STrong')

@app.route("/ap/jobs")
def list_job():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)