# importing libraries
from flask import Flask, render_template, redirect, request
import mysql.connector
import os
sql_passwd = os.environ.get("sql_key")



app = Flask(__name__)

# ------------------------------
# rendering applications
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/admin')
def about():
	return render_template('admin.html')

@app.route('/faculty')
def faculty():
	db = mysql.connector.connect (
	host="localhost",
	user="root",
	password=sql_passwd,
	database="lms"
	)
	cursor = db.cursor()
	cursor.execute("SELECT * FROM books")
	book_names = cursor.fetchall()
	return render_template('faculty.html', book_names = book_names)

@app.route('/student', methods=['GET', 'POST'])
def student():
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		password=sql_passwd,
		database="lms"
	)
	cursor = db.cursor()
	cursor.execute("SELECT * FROM books")
	book_names = cursor.fetchall()
	return render_template('student.html', book_names = book_names)
# ------------------------------

# populating database
# lms database -> books table
@app.route('/add', methods=['GET', 'POST'])
def add():
	print("Function running")
	# print(request.form['book-name'])
	book_name = request.form['book-name']
	book_author = request.form['book-author']
	stock = request.form['stock']

	connection = mysql.connector.connect(host='localhost', user='root', password=sql_passwd, database='lms')
	cursor = connection.cursor()

	cursor.execute('INSERT INTO books (NAME, AUTHOR, STOCK) VALUES (%s, %s, %s)', (book_name, book_author, stock))
	connection.commit()
	return f'''Book added successfully
	Book name: {book_name}
	Book author: {book_author}
	Stock: {stock}'''

if __name__ == '__main__':
	app.run(debug=True)