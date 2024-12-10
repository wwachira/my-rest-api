## Author
L. W.Wachira
## in your terminal import request 
pip3 install requests

## print(response)
It should give you a response 200 - okay

## print(response.json()) method
To get all the actual data.

## print specifics you can iterate after request.get in the loop
* Convert the response to JSON
data = response.json()

* Ensure the response contains 'items'

if 'items' in data:
    for item in data['items']:
        # Check if 'owner' exists in the item
        if 'owner' in item:
            owner = item['owner']
            # Print the 'link' and 'account_id' if they exist
            print(owner.get('link', 'No link available'))
            print(owner.get('account_id', 'No account ID available'))
            print()
else:
    print("No items found in the response.")

# How we can create our own API
* create a folder here its api_buildd, enter the folder and run the following commands to enter our virtual environment.
python3 -m venv .venv (creates a virtual env in .venv folder)
source .venv/bin/activate (to activate the folder)
pip3 install flask (to install dependancies in our venv)
* Downloading flask-3.0.3-py3-none-any.whl (101 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.7/101.7 KB 198.6 kB/s eta 0:00:00
pip3 install flask-sqlalchemy (meant to work with the database)
* Downloading SQLAlchemy-2.0.36-cp38-cp38-manylinux_2_17_x86_64.
manylinux2014_x86_64.whl (3.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 499.8 kB/s eta 0:00:00
python3 -m pip install --upgrade pip (to upgrade pip in our venv)
* Downloading pip-24.3.1-py3-none-any.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 504.3 kB/s eta 0:00:00

# we can put our dependancies in a file
pip3 freeze > requirements.txt

# create our file application.py
touch application.py

# to run our application (always make sure you are in .venv)
export FLASK_APP=application.py
export FLASK_ENV=development
flask run

# to connect to a DB, we will consider an ORM
quit .venv terminal => ctrl+c
 python3 (in the terminal)
  * After updating you model on application.py:
 from application import db (in the terminal for python3) 
 from application import db,app,  Drink
 >>> from application import db, app
>>> with app.app_context():
...    db.create_all()
print("Database tables created successfully!")

