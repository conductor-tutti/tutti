***** Tutti project tutorial *****

[Prerequisite]
- Git with Github account
- Google App Engine Launcher
- MySQL Server

[Flask]
1. Init your Github repository with 'git init'
2. Pull Github repository https://github.com/conductor-tutti/tutti
3. Install Python Setup Tools (https://pypi.python.org/pypi/setuptools), note that Python pip should be installed prior to this step
4. Install Python libraries using a command 'pip install -t lib -I flask-sqlalchemy flask-migrate flask-oauth'.
- This should be run at project [ROOT] directory where '.git' folder is located
5. Install a Python library MySQLdb (ref: http://stacklion.com/questions/detail/54)

[MySQL]
1. Install MySQL Server
2. Create database named 'local_tutti'
3. Configure MySQL DB connection by changing '[ROOT]/settings.py'

[Google App Engine]
1. Place Google App Engine configuration files in [ROOT] 
- This file might be given by Seulki Kim
2. Install Google App Engine (GAE) Launcher
3. Using GAE launcher, load project root directory as existing project
4. Launch and connect to 'localhost:8080'
