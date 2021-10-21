# Dev Dependencies

-   PostgresSQL==13.3
-   Python==3.9.6
-   Node.js==14.17.4
    Make sure you have the appropriate dev dependencies installed locally before proceeding

# Postgres Setup:

-   Downloaded [PostgresSQL](https://www.postgresql.org/download/windows/) (here's a great [guide](https://www.postgresqltutorial.com/install-postgresql/) to setting it up).
-   Verify postgres is successfully installed by typing `psql` in cmd terminal (not powershell or bash/linux).
    -   If you get an error after trying the `psql` command, you'll likely need to add your PostgreSQL bin folder to your system PATH environment variable.
    -   If the above does not work, try `export PATH="C:\Program Files\PostgreSQL\13\bin:$PATH"` in your terminal (replace the path with whatever the path destination is for your PC)
-   login to postgres on the command line (typically `psql -U root` or `psql -U postgres`), then enter the password used in initial setup.
-   Once inside the PSQL shell, create a new database:
    `CREATE DATABASE questingdb;`
-   note: you can name it whatever you want; it doesn't have to be "questdb".
-   note2: don't forget the `;` at the end.
-   quit the psql terminal with `\q`

# Local Setup

-   If using virtualenv package: first install globally.
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

# GIT Workflow

The most up-to-date and stable branch should _always_ be Master. _Never_ commit directly to master, only approved/reviewed merges.

##### Start a new feature branch:

-   Switch to the master branch with:`git switch master`
-   Fetch all changes (update your local repo) from remote:`git pull master`
    -   Optional: If you'd like to update all branches in your local repo:`git pull`
-   Create and switch to a new branch (READ Branch naming convention below before proceeding): `git checkout -b Feature/10-Update-Readme-File`

###### Branch Naming Conventions

-   To keep things organized, name branches accordingly: `<TypeOfBranch>/<TrelloNumber>-<Brief-Description-of-Branch>`
-   TypeOfBranch:
    -   Use "Feature" for new features, such as creating models, folders, functionality, etc
    -   Use "Bug" for fixing an existing feature
    -   Use "Hotfix" if the branch is for minor/preferential modifications to existing (working) areas of the code
-   TrelloNumber: All branches should have a trello ticket # to go along with it. If there is none, create one first.
    -   Note: For example, if the trello ticket is 3; use 3. If the same trello ticket requires revisiting
        a second/third/fourth time after a merge has already taken place, use 3.1, 3.2, 3.3, etc (or create a NEW trello ticket)
-   Brief-Description-of-Branch: Keep it brief but to the point.
    -   Note: For example, if the branch involves integrating Google Translate API - use "Add-Google-Translate"
-   Full examples:
    `git checkout -b Feature/12-Setup-React-Native`
    `git checkout -b Bug/34-Fix-Dropdown-Menu`
    `git checkout -b Hotfix/23-Text-Font`
    `git checkout -b Bug/34.1-Fix-Dropdown-Menu-AGAIN-ugh`
    `git checkout -b Feature/12.1-Reconfigure-React-Native-Setup`

###### Git Workflow

With multiple developers working on the same project, we're bound to run into version control conflicts.
Use the following workflow to prevent that:

-   Always `git pull master` before checking out to a new branch
-   Before setting up a pull request to master remotely, always follow the following steps:
    1. Switch to your current feature/bug/hotfix branch you'd like to push.
    2. `git pull` to update your local repository.
    3. `git merge master` to integrate any changes that may have been merged to master while you were working on your branch.
    4. `git push -u origin The-Name-Of-Your-Current-Branch` to push your current branch to the remote repository.
    5. Head over to the Questing repository on github.com
    6. Create a PR to merge your branch into master.
    7. Optional (But HIGHLY recommended): Ping another developer the URL to your PR to review before merging.
    8. Accept merge request and merge on github.com
    9. Update relevant Trello card
    10. Notify the group of a merge on discord (so that everyone can do a `git pull` and `git merge master` to update whatever they're working on)\

TODO: Create a development branch to be used on a staging server -> Update git workflow to incorporate development branch.

# Current File Structure WIP:

```
├───frontend (Everything Front-End Related including static files)
│   app.py
│   local_settings.py (Settings extension *DO NOT INCLUDE IN VERSION CONTROL*)
│   settings.py
│   urls.py (Base URL Routing *can extend routes within other apps*)
│
├───migrations (Auto-generated with Flask-Migrate to allow migration commits to version control)
│   │   alembic.ini
│   │   env.py
│   │   README
│   │   script.py.mako
│   │
│   ├───versions
│   └───__pycache__ (NOT COMMITTED TO VERSION CONTROL)
│           env.cpython-39.pyc
│
├───models (A single file per model; file should also include serializer object)
│   │   user.py
│   │   __init__.py
│   │
│   └───__pycache__ (NOT COMMITTED TO VERSION CONTROL)
│           user.cpython-39.pyc
│           __init__.cpython-39.pyc
│
├───utils (Utility functions and classes not belonging to a specific view/model)
│       __init__.py
│
├───views (Views function logic goes here)
│   │   test_db.py
│   │   __init__.py
│   │
│   └───__pycache__ (NOT COMMITTED TO VERSION CONTROL)
│           test_db.cpython-39.pyc
│           __init__.cpython-39.pyc
│
└───__pycache__ (NOT COMMITTED TO VERSION CONTROL)
        app.cpython-39.pyc
        local_settings.cpython-39.pyc
        settings.cpython-39.pyc
        urls.cpython-39.pyc
```
