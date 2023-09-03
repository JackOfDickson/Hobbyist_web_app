# Hello user! Welcome to my project!
This is a refactor of my first project at CodeClan which uses python3, flask, postgresql and now includes SQLAlchemy (was using psycopg2 in the first version)!
The application runs a webpage on a browser and manages members lessons and bookings.

## The brief
My brief was to make an app that could:
- Create and edit lessons within the app
- Create and edit members within the app
- To be able to book members into lessons
- Display a list of all upcoming lessons
- Display a list of members attending each lesson

## How to get it running!

### What you will need
Python3 and postgresql installed on your machine

Check you can access postgresql databases through the psql command or a UI like postico if you are installing it for the first time.

Then you will need the following pip3 packages:
Flask, python-dotenv, flask-SQLAlchemy, flask-migrate

You can install them with the following commands:
```
pip3 install Flask
pip3 install python-dotenv
pip3 install flask-sqlalchemy
pip3 install flask-migrate
pip3 install pyscopg2
```

### Getting Started

Step 1 - Set up a database so run the following command in your terminal:
```
createdb hobbyist
```
Step 2 - Adjust code so that the flask application can find the database:

So in line 6 in app.py you want to change the following code
```
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/hobbyist"
```

and change `user` to your username for postgres (you can check by the command `psql` and your username will show up)

Step 3 - Populate the database with tables and seed data, this can be done by typing in your terminal (at the top level of the project) the following commands:
```
flask db upgrade
flask seed
```
Step 4 - Run the application with the command:
```
flask run
```
Step 5 - Open your browser (I would recommend chrome) and enter the address of the local host port (If unsure look at your terminal look at the line "Running on" and copy and paste the url into the browser).
If you need to close the app you can press control and c to stop the webpage from running.

## Navigating the website!
Once on the website you can click the following on the header of the page:
- Hobbyist:
Brings you to the homepage which also has some instructions for navigating the website

- Current Members:
Shows the list of the members on the system. Clicking on them shows you more details such as what lessons they are apart of and options to edit the member, cancel bookings for lessons they have signed up or delete the member entirely (deleting them will also delete the bookings associated with them).

- Upcoming Lessons:
Shows the list of all the lessons and a date next to them. Clicking on them will also show more details like lesson capacity and the lesson's attendees as well as options to edit the lesson or cancel the lesson (cancelling the lesson also deletes the bookings made for it)

- Book a Lesson:
Brings up a form where an existing member and lesson can be selected to register them for the lesson

- New Member Sign-up:
Brings up a form to register a new member

- Create a new lesson
Brings up a form to create a new lesson
