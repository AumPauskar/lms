# importing libraries
from flask import Flask, render_template, redirect, request # backend
import mysql.connector 										# db connector
import os 													# for getting environment variable
import datetime												# getting current date
import csv													# writing to csv file


# gets sql password from environment variable
# refer README.md
sql_passwd = os.environ.get("sql_key") 	
date = datetime.date.today()
final_date = date.today() + datetime.timedelta(days=15)


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
	# connecting to the sql db
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		password=sql_passwd,
		database="lms"
	)

	# retriving book names
	cursor = db.cursor()
	cursor.execute("SELECT * FROM books") # operation on books table
	book_names = cursor.fetchall()

	return render_template('student.html', book_names = book_names)

@app.route('/student_borrow', methods=['GET', 'POST'])
def student_borrow():
	# connecting to the sql db
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		password=sql_passwd,
		database="lms"
	)
	cursor = db.cursor()

	# getting form inputs
	name = request.form["name"]
	id = request.form["id"]
	type = "STUDENT"

	for i in range(1, 7):
		book_name = request.form[f"book-{i}"]
		print("Book name: ", book_name)

		# retrieving book id
		query = 'SELECT book_id FROM books WHERE name = %s'
		cursor.execute(query, (book_name,))
		book_id = cursor.fetchone()
		book_id = str(book_id[0]) # converts from tuple to string
		
		# checking if book is available or out of stock
		query = 'SELECT stock FROM books WHERE name = %s'
		cursor.execute(query, (book_name,))
		stock = cursor.fetchone()
		stock = str(stock[0]) # converts from tuple to string

		if stock == '0':
			# code breaks over here due to return statement
			return "Book out of stock"
		
		# reducing the stock by 1
		stock = int(stock) - 1
		cursor.execute('UPDATE books SET stock = %s WHERE name = %s', (stock, book_name))

		# adds record in book_borrowings
		cursor.execute('INSERT INTO book_borrowings (BOOK_ID, BORROWER_ID, BORROWER_TYPE, BORROWED_DATE, DUE_DATE) VALUES (%s, %s, %s, %s, %s)', (book_id, id, type, date, final_date))
		db.commit()

		# writing to csv file student - record.csv
		with open('student-record.csv', 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([name, id, book_name, book_id, date, final_date])

	return "Book added"

# inserting values to db

@app.route('/faculty_borrow', methods=['GET','POST'])
def faculty_borrow():
	# connecting to the sql db
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		password=sql_passwd,
		database="lms"
	)
	cursor = db.cursor()

	# getting form inputs
	name = request.form["name"]


	id = request.form["id"]
	type = "FACULTY"

	book_names = []
	for i in range(1, 19):
		book_name = request.form[f"book-{i}"]
		if book_name:
			book_names.append(book_name)

	for book_name in book_names:
		# retrieving book id
		query = 'SELECT book_id FROM books WHERE name = %s'
		cursor.execute(query, (book_name,))
		book_id = cursor.fetchone()
		book_id = str(book_id[0]) # converts from tuple to string

		# checking if book is available or out of stock
		query = 'SELECT stock FROM books WHERE name = %s'
		cursor.execute(query, (book_name,))
		stock = cursor.fetchone()
		stock = str(stock[0]) # converts from tuple to string

		if stock == '0':
			# code breaks over here due to return statement
			return "Book out of stock"
		
		# reducing the stock by 1
		stock = int(stock) - 1
		cursor.execute('UPDATE books SET stock = %s WHERE name = %s', (stock, book_name))

		# adds record in book_borrowings
		cursor.execute('INSERT INTO book_borrowings (BOOK_ID, BORROWER_ID, BORROWER_TYPE, BORROWED_DATE, DUE_DATE) VALUES (%s, %s, %s, %s, %s)', (book_id, id, type, date, final_date))
		db.commit()

	return "Book added"

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

# deleting books from database - admin panel
@app.route('/delete', methods=['GET', 'POST'])
def delete():
	print("Delete function running")
	book_id = request.form['book-id']

	# delete books from books table via book_id
	db = mysql.connector.connect(host="localhost",
		user="root",
		password=sql_passwd,
		database="lms"
	)
	cursor = db.cursor()
	cursor.execute('DELETE FROM books WHERE book_id = %s', (book_id,))
	db.commit()
	return f"Book id with {book_id} deleted"

# changing stock of books - admin panel
@app.route('/change_stock', methods=['GET', 'POST'])
def change_stock():
	print("Change stock function running")
	book_id = request.form['book-id']
	stock = request.form['stock']

	# change stock of books from books table via book_id
	db = mysql.connector.connect(host="localhost",
		user="root",
		password=sql_passwd,
		database="lms"
	)
	cursor = db.cursor()
	cursor.execute('UPDATE books SET stock = %s WHERE book_id = %s', (stock, book_id))
	db.commit()
	return f"Book id with {book_id} updated with stock {stock}"


if __name__ == '__main__':
	app.run(debug=True)