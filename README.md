# Djangosite
Website of duggal Industries.  

<h4> Create a virtual environment</h4>
$ sudo apt-get install virtualenv 

$ mkdir somename

$ cd somename 

$ virtualenv .

$ source bin/activate

<h4> use deactivate command whenever needed</h4>

<h4>Clone the repository</h4>

$ cd Djangosite

$ pip install -r requirements.txt

<h4>Open the settings file in favourite browser</h4>

path : Djangosite/duggal/duggal/settings.py

<h4>Edits</h4>

add the specifications of your email in line 38-39

add the specifications of your database in line 101-107

<h4>when in Djangosite/duggal</h4>

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver

<h4>Open the browser for the link</h4>

127.0.0.1:8090