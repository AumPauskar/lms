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
The raw SQL file is already provided in the project. To create a databse and create all the tables within it run 
```
source C:\...<full path>...\sql_raw.sql;
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
## Notes
The software is created within a python virtual environment and using a Windows NT kernel (Win 11).