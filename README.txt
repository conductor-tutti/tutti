***** Tutti project tutorial *****

[Prerequisite]
- Git with Github account
- Google App Engine Launcher
- MySQL Server

[Flask]
1. Init your Github repository using a command 'git init'
2. Pull Github repository https://github.com/conductor-tutti/tutti
3. Install Python Setup Tools (https://pypi.python.org/pypi/setuptools), note that Python pip should be installed prior to this step
4. Install Python libraries using a command 'pip install -t lib -I flask flask-sqlalchemy flask-migrate flask-oauth'.
- This should be run at project [ROOT] directory where '.git' folder is located
5. Install a Python library MySQLdb (ref: http://stacklion.com/questions/detail/54)
- If using .exe install for this, the libraries will be installed in '[PYTHON]/Lib/site-packages'. Copy and paste all the files and folder containing 'MySQL' including compiled files such as pyc

[MySQL]
1. Install MySQL Server
2. Create database named 'local_tutti'
3. Configure MySQL DB connection by changing '[ROOT]/settings.py'
4. Initialize local db: 'python manager.py db init'
- This command uses flask library installed in '[PYTHON]/Lib/site-packages', so you may need to install flask-related libraries globally by using 'pip install flask flask-sqlalchemy flask-migrate flask-oauth' instead of 'pip install -t lib ...' command
5. Migrate db: 'python manager.py db migrate'
- Ready for creating initial tables
6. Upgrade db: 'python manager.py db upgrade'
- This creates tables

[Google App Engine]
1. Place Google App Engine configuration files in [ROOT] 
- This file might be given by Seulki Kim
2. Install Google App Engine (GAE) Launcher
3. Using GAE launcher, load project root directory as existing project
4. Launch and connect to 'localhost:8080'


[Etc]
1. Make sure that the code is written as below in '[ROOT]\app\__init__.py' unless you can destroy running tutti application on production
- RIGHT: app.config.from_object("app.settings.Development") 
- WRONG: app.config.from_object("app.settings.Production")