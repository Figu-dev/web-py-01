from flask import Flask, render_template, jsonify

app = Flask(__name__)

## creamos una lista con los trabajos para mostrar de forma dinámica
JOBS = [
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Zaragoza, Spain',
    'salary': '20.000 €'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Madrid, Spain'
  },
  {
    'id': 4,
    'title': 'Backtend Engineer',
    'location': 'Bilbao, Spain',
    'salary': '50.000 €'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
