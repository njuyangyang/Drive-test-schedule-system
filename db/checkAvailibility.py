

import sqlite3 as lite
import sys
import automail

#input_dict is a dictionary data structure
def checkAvailibility(input_dict):

	#wrap the database into an object
	con=lite.connect('development.sqlite3')


	with con:
		cur=con.cursor()
		cur.execute("SELECT * FROM users")

		rows=cur.fetchall()

		for row in rows:
			print row
			name=row[1]
			email=[row[2]]
			expect_date=row[3]

			if expect_date in input_dict and input_dict[expect_date]==1:
				automail.automail(email)
				cur.execute("DELETE FROM USERS WHERE username=?",(name,))
				print (name, " is delete")
			else:
				continue

