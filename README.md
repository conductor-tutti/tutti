# Prerequisite
- Git with Github account
- Google App Engine Launcher
- MySQL Server

# Flask
* Init your Github repository using a command 'git init'
* Pull Github repository https://github.com/conductor-tutti/tutti
* Install Python Setup Tools (https://pypi.python.org/pypi/setuptools), note that Python pip should be installed prior to this step
* Install Python libraries using a command 'pip install -t lib -I flask flask-sqlalchemy flask-migrate flask-oauth'. This should be run at project [ROOT] directory where '.git' folder is located
* Install a Python library MySQLdb (ref: http://stacklion.com/questions/detail/54). If using .exe install for this, the libraries will be installed in '[PYTHON]/Lib/site-packages'. Copy and paste all the files and folder containing 'MySQL' including compiled files such as pyc

# MySQL
* Install MySQL Server
* Create database named 'local_tutti'
* Configure MySQL DB connection by changing '[ROOT]/settings.py'
* Initialize local db: 'python manager.py db init'. This command uses flask library installed in '[PYTHON]/Lib/site-packages', so you may need to install flask-related libraries globally by using 'pip install flask flask-sqlalchemy flask-migrate flask-oauth' instead of 'pip install -t lib ...' command
* Migrate db: 'python manager.py db migrate'. Ready for creating initial tables
* Upgrade db: 'python manager.py db upgrade'. This creates tables

# Google App Engine
* Place Google App Engine configuration files in [ROOT] This file might be given by Seulki Kim
* Install Google App Engine (GAE) Launcher
* Using GAE launcher, load project root directory as existing project
* Launch and connect to 'localhost:8080'

# Etc
* Make sure that the code is written as below in '[ROOT]\app\__init__.py' unless you can destroy running tutti application on production
  * RIGHT: app.config.from_object("app.settings.Development") 
  * WRONG: app.config.from_object("app.settings.Production")
  * You can use code below for the above confusion

```
if os.environ['SERVER_SOFTWARE'].startswith('Development'):
    app.config.from_object("app.settings.Development")
else:
    app.config.from_object("app.settings.Production")
```