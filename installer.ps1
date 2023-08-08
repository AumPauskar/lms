# NOTE THIS APP IS STILL IN TESTING PHASE DO NOT RUN IT

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Installing..."

    # Get the latest version of Python
    $python_version = (Invoke-WebRequest "https://www.python.org/downloads/release/latest/").Content

    # Download the Python installer
    $python_installer = "python-${python_version}-amd64.exe"
    Invoke-WebRequest "https://www.python.org/ftp/python/${python_version}/${python_installer}" -OutFile $python_installer

    # Install Python
    Start-Process $python_installer -Wait
}

# Write a message to the user
Write-Host "Python has been installed."

# Get the latest MySQL version
$latest_mysql_version = (Invoke-WebRequest "https://dev.mysql.com/downloads/mysql/").Content

# Download the MySQL installer
$mysql_installer = "mysql-installer-community-${latest_mysql_version}-winx64.msi"
Invoke-WebRequest "https://dev.mysql.com/get/Downloads/MySQL-installer/community/releases/${latest_mysql_version}/${mysql_installer}" -OutFile $mysql_installer

# Install MySQL
Start-Process $mysql_installer -Wait

# Write a message to the user
Write-Host "MySQL has been installed."


# Install Flask, Jinja2, and MySQL Connector Python
pip install flask jinja2 mysql-connector-python

# Set up a user environment variable
$sql_key = Read-Host "Enter the value for the SQL_KEY environment variable:"
[Environment]::SetEnvironmentVariable("sql_key", $sql_key, "User")

# Write a message to the user
Write-Host "The SQL_KEY environment variable has been set to $sql_key."
