# Company

## Contribution

If you want to contribute to this project then please use the dev branch, create a new branch or fork this project

## Virtual Enviroment
You should create and activate virtual environment:

```
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
```

If there is a problem [consult this](https://virtualenv.pypa.io/en/stable/installation/)

## Install dependecises

When in your virtualenviroment just run

```
pip install -r requirements.txt
```

## Install application
To install the required configs for this application just run the install.py script.
This will also make an admin user (usr:admin, pass: admin) witch is used on the site.

## Run application

open the terminal and write ```flask run``` then browse to [locaclhost:5000](http://localhost:5000)