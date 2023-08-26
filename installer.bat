@echo off

rem Install Python
echo Installing Python...
python -m pip install --user python

rem Set up Python environment variables
echo Setting up Python environment variables...
set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts

rem Install MySQL
echo Installing MySQL...
echo.
msiexec /i "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql-installer.msi" /qn /norestart

rem Configure MySQL
echo Configuring MySQL...
echo.
mysqld --initialize-insecure

rem Set up MySQL environment variables
echo Setting up MySQL environment variables...
set PATH=%PATH%;C:\Program Files\MySQL\MySQL Server 8.0\bin
set MYSQL_HOME=C:\Program Files\MySQL\MySQL Server 8.0

rem Install Flask and MySQL-connector-python via pip
echo Installing Flask and MySQL-connector-python via pip...
python -m pip install flask mysql-connector-python

rem Set up sql_key environment variable and ask the user for the password
echo Setting up sql_key environment variable...
set sql_key=
set /p sql_key="Enter the MySQL password: "

rem Make a CSV called "student_record.csv" in the same directory and write the following into it: "Name,Id,Book name,Book id,Borrowed date,Due date"
echo Making a CSV called "student_record.csv" in the same directory and writing the following into it: "Name,Id,Book name,Book id,Borrowed date,Due date"
echo.
echo Name,Id,Book name,Book id,Borrowed date,Due date > student_record.csv
