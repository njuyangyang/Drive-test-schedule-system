Required Environment:
Firefox Browser
Ruby on Rails
Ruby(4.2.2)
Python
#############################################################################
Open the terminal:

Clone the repo: 
$git clone https://github.com/njuyangyang/sample_app-1.git ~/sample_app

Change directory:
$cd ~/sample_app
############################################################################
Set the front-end environment:

Installing Rails with a specific version number:
gem install rails -v 4.2.2

install the gems using:
$bundle install —-without production

migrate the database:
$ bundle exec rake db:migrate

run the local web server:
$rails s

Now the application should be available on the local server:
http://localhost:3000

Click the button:Get Started Now!

Enter Your Information:
Your name, Your email, and the expected date you want to take the driving license test(According to the website of DPS, you can only input the date 90 days from now)
And then click create
#############################################################################
Start the back-end:

Change directory:
$cd ~/sample_app/db

execute the controller.py:
$python controller.py



