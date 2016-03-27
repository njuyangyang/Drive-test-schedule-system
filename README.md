#HackUTD : Find Available Driving Test Appointment

##Required Environment

1. Firefox Browser
2. Ruby on Rails
3. Ruby(4.2.2)
4. Python

##How to setup the App

###downlowad the code

Open the terminal:

Clone the repo: 
$git clone https://github.com/njuyangyang/sample_app-1.git ~/sample_app

Change directory:
$cd ~/sample_app

###Set the front-end environment

Installing Rails with a specific version number:
gem install rails -v 4.2.2

install the gems using:
$bundle install —-without production

migrate the database:
$ bundle exec rake db:migrate

run the local web server:
$rails s

![terminal](/screenshot/terminal.png)

Now the application should be available on the local server:
http://localhost:3000

Click the button:Get Started Now!

Enter Your Information:
Your name, Your email, and the expected date you want to take the driving license test(According to the website of DPS, you can only input the date 90 days from now)
And then click create


###Start the back-end

Change directory:
$cd ~/sample_app/db

execute the controller.py:
$python controller.py

**warnning**

1. You will receive a notification only if your expecting date is available. For test purpose, You should check the available date in DPS website or our datebase before you type in your information.
2. so far, this application is used for Byran DPS only.

**declaration**
1. To obey the rules, we declare that the Front end UI framework is create several days ago, which we used in another project.




