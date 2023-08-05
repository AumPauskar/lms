from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/admin')
def about():
	return render_template('admin.html')

@app.route('/faculty')
def contact():
	return render_template('faculty.html')

@app.route('/student')
def student():
	return render_template('student.html')

if __name__ == '__main__':
	app.run(debug=True)