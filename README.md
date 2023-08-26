# Library management system

## Prerequisites
**NOTE:** Before installing the packages please go through the **setting up** process, since these programs can be installed natively or via virtual environment.

- Python and pip
	1. flask `pip install flask`
	2. jinja2 `pip install Jinja2`
	3. mysql connector `pip install mysql-connector-python`
- MySQL (tested with v 8.0.33)

## Setting up

- Environment variables
To set up this application you need to set up the environment variable in the windows machine. To do this search environment variable in the search menu and add a new key in it. The key must be named **sql_key**. Note that you might want to restart you comptuer after setting up the environment variable key.

- SQL
The raw SQL file is already provided in the project in case the tables needed to be populated for demonstration or to check the programs integrity. To create a database and create all the tables within it run. Make sure to run these commands while inside the MySQL server.

To open my sql server, open the terminal and run this command
```
mysql -u root -p
```
Then your password can be inserted to run this command

For the initial setup
```
source C:\...<full path>...\sql_raw_files\initial_setup.sql;
```
To insert all the datasets for testing purposes you can either insert the data via the admin panel or insert via the preconfigured file. To run it run the following command.
```
source C:\...<full path>...\sql_raw_files\populating_tables.sql
```

- Creating a virtual environment

Although creation of a virtual environment is not necessary and the program can be installed with all the packages running natively, creation of virtual environment makes sure that there are no conflicts between your packages.

Creation
```
py -m venv env
```

Activation in windows **command prompt**
```
env\Scripts\activate.bat
```

Activation in windows **powershell**
```
env\Scripts\activate.ps1
```

## Assumptions
1. The return date is 15 days after the borrowing date
2. Student ID is incremented for easy use

## UI
Here are some of the screenshots of the User Interface of the project
- Home page
![home page](docs/screenshots/home%20page.png)

- Adding books
![adding books students](docs/screenshots/adding%20books%20-%20student.png)
![adding books faculty](docs/screenshots/adding%20books%20-%20faculty.png)

- Admin panel
![admin panel](docs/screenshots/admin%20-%20add%20books.png)

This is the structure 
## Notes
The software is created within a python virtual environment and using a Windows NT kernel (Win 11).

a copy of this project can be found at https://github.com/AumPauskar/lms