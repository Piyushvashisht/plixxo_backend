# Plixxo
The perfect platform for brands and digital media influencers to connect and produce the most awesome campaigns!

## Installation Backend
Use the package manager pip (https://pip.pypa.io/en/stable/) to install the requirements
```bash
$ pip install requirements.txt
```

## Database
Create a postgres database with
```bash
name="plixxo" 
password="pankaj"
```

## Migrations
Initially reset the migrations by using the following command
```bash
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc"  -delete
```
Then create new migrations using the following command
```bash
$ python manage.py makemigrations
```
The execute the migrations using the following command
```bash
$ python manage.py migrate
```
## Installing the aws shell
The aws-shell requires python and pip to install. You can install the aws-shell using pip:
Install the aws-shell using the following command
```bash
$ pip install aws-shell
```
## Configuring the aws-shell
Now you have to configure the aws shell, inorder to do that open your terminal and start the aws shell using the following command
```bash
$ aws-shell
```
Then run the configure command to configure the shell
```bash
aws> configure
```
## Installing the aws packages
The backend code requires some aws-boto3 packages to be installed.
They can be installed using pip.
Execute the following command to install the aws-boto3 packages
```bash
$ pip install PushToBucket-0.1.dev0-py3-none-any.whl
$ pip install PlixxoActivity-0.1.dev0-py3-none-any.whl
```
## Executing the backend
After completing the above steps now you are ready to start the server.
Run the server using the following command
```bash
$ python manage.py runserver
```
## Installation frontend
If you haven't installed npm on your local then install it using the following command
```bash
$ npm install
```
Then after successfully installing the npm package manager build the frontend using the following command
```bash
$ npm build
```
Then finally start the frontend using the following command
```bash
$ npm start
```