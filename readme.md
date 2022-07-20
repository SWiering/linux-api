### Required file
Make sure the file: https://gist.github.com/beetlerom/1c2d8519fd8957a123a829a1597e97de is downloaded and located in the root folder of the project

### Preperation
to install the requirements for this project, type the following in the console in the directory of the python project:
```
pip install -r requirements.txt
```
or
```
python -m pip install -r requirements.txt
```

### Starting it
in order to start the flask api server locally execute the following commands in the python project:

windows:
```
$ set flask_app=app
$ set flask_env=development
$ flask run
```
ubuntu/linux:
```
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```