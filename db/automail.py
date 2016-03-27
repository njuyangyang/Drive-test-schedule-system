#This function is uesed as sending email to the users
#You need to input "EMAIL" address you want to send and the "EMAIL" must be a list!
import smtplib
def automail(EMAIL):
	PASSWORD = "2453okok"

	FROM = "autonotificationfromhackutd@gmail.com"

	TO = EMAIL # must be a list

	SUBJECT = "Hello!"

	TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

	message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail


	mailserver = smtplib.SMTP("smtp.gmail.com", 587) 
	mailserver.ehlo() 
	mailserver.starttls() 
	mailserver.ehlo() 
	mailserver.login(FROM , PASSWORD) 
	mailserver.sendmail(FROM, TO, message)
	mailserver.close() 




