# Flask Hello World Project



A simple Flask scaffold project implementing:
- configuration variables from .env file
- app factory
- blueprints
- templating
- routes
  - GET `/`
  - GET `/hello`
  - GET `hello/<name>`
  - GET `sayhello?name=`
  - POST `sayhello` with `username` in form


## Table of Contents
- [Flask Hello World Project](#flask-hello-world-project)
  - [Table of Contents](#table-of-contents)
  - [File structure](#file-structure)
  - [Setup (Windows)](#setup-windows)

## File structure

```toml
project/
|   .env # configuration variables
|   .gitignore
|   README.md
|   requirements.txt
|   run.py # app runner
|   
+---apps
|   |   __init__.py # app factory
|   |   
|   +---hello # hello blueprint folder
|   |   |   __init__.py # hello blueprint and routes
|   |   |   
|   |   +---templates # templates for hello blueprint
|   |   |   \---hello
|   |   |           index.html
```


## Setup (Windows)

```
git clone 
cd folder
virtualenv venv
venv\Scripts\activate
copy env.sample .env # create sample .env file
```

To run:
```
flask run
```

