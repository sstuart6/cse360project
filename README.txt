CSE 360 Fall 2014 Image Uploader Project README“Look at this Shit!”
Demo video link:(add later)
Group Members: Charles Lima, Ted Work, Shelby StuartMost of the functionality of the project should be there, the only thing that I was having trouble with was the editing of photos (brightness). ——————————————————————————————————————————————————————————————Set up of the project I set the project up in a mac, so these are my instructions1. Create a virtual environment and activate it.

2. place source and static folders in virtual environment. 

3. to install the required packages, type ‘pip install -r requirements.txt’ 
this will read every line of the file and install whatever is written. 

4. enter the src folder and run ‘python manage.py migrate’ to make sure the models are synched to the database. 

5. run ‘python manage.py runserver’ to turn on the server.

6. to run the functionality tests, you must enter the signups folder and runeach test individually.
list of commands to run for all functionality tests
python login_test.py
python register_test.py
python logout_test.py
python navigation_test.py
python profile_test.py
python upload_test.py——————————————————————————————————————————————————————————————Once the http address appears below the runserver command, you can copy
it and paste it into the address bar of your browser and the site will render.
The functionality is described by the youtube video at the top of the page. 