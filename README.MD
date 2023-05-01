# Hello user! Welcome to my project!
This is a application that uses python3, postgresSQL and flask which runs a webpage on a browser and manages members lessons and bookings.

## The brief
My brief was to make an app that could:
- Create and edit lessons within the app
- Create and edit members within the app
- To be able to book members into lessons
- Display a list of all upcoming lessons
- Display a list of members attending each lesson

## How to get it running!
Step 1 - Set up a database so run the following command in your terminal:
```
createdb hobbyist
```
Step 2 - Navigate to the hobbyist file location in your terminal and run the command:
```
psql -d hobbyist -f db/hobbyist.sql
```
Step 3 - In your terminal seed the data by running the console.py which by running the following command:
```
python3 console.py
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
Brings you to the homepage which also has some intructions for navigating the website

- Current Members:
Shows the list of the members on the system. Clicking on them shows you more details such as what lessons they are apart of and options to edit the member or delete them (deleting them will also delete the bookings associated with them)

- Upcoming Lessons:
Shows the list of all the lessions and a date next to them. Clicking on them will also show more details like lesson capacity and the lesson's attendees as well as options to edit the lesson or cancel the lesson (cancelling the lesson also deletes the bookings made for it)

- Book a Lesson:
Brings up a form where an existing member and lesson can be selected to register them for the lesson

- New Member Sign-up:
Brings up a form to register a new member

- Create a new lesson
Brings up a form to create a new lesson

- Manage Bookings
Brings up a list of bookings made which can be cancelled by clicking the "x" underneath them
