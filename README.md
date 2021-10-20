# Dev Dependencies

-   PostgresSQL==13.3
-   Python==3.9.6
-   Node.js==14.17.4
    Make sure you have the appropriate dev dependencies installed locally before proceeding

# Postgres Setup:

-   Downloaded [PostgresSQL](https://www.postgresql.org/download/windows/) (here's a great [guide](https://www.postgresqltutorial.com/install-postgresql/) to setting it up)
-   Verify postgres is successfully installed by typing `psql` in cmd terminal (not powershell or bash/linux)
-   login to postgres on the command line (typically `psql -u root` or `psql -u postgres`), then enter the password used in initial setup
-   Once inside the PSQL shell, create a new database:
    `CREATE DATABASE questingdb;`
-   note: you can name it whatever you want; it doesn't have to be "questdb"
-   note2: don't forget the `;` at the end.
-   quit the psql terminal with `\q`

# Local Setup

-   If using virtualenv package: first install globally
    `pip install virtualenv`
-   Next navigate to root directory at `.\Questing\`
-   Create your virtual env (this will create a virtual environment folder at the root named "venv"):
    `python -m venv venv`
-   Activate your environment:
    `\venv\Scripts\activate`
-   Next install requirements:
    `pip install -r requirements.txt`
-   Last, navigate to `.\backend\` and create your `local_settings.py` file. Within that file, paste the following code:

```
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
POSTGRES_DATABASE_NAME = ''
DEVELOPMENT = True
```

-   You'll need to insert the appropriate strings that you used to setup postgres; for example:

```
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'password'
POSTGRES_DATABASE_NAME = 'questingdb'
```
