#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 06:42:50 2016

@author: iphyer

output :
return value

1 means sth changed
0 nothing changed
"""

#import needed package
from selenium import webdriver # web action
from pyvirtualdisplay import Display
from datetime import date
import BeautifulSoup as bs
import sqlite3
import pickle

# function setup

def htmltableGetinfomation(websource,data_page):
    """
    get information from html source

    input : html source code

    output : dict of data and availibility

    """
    month2num = { 'January' : 1, 'February': 2,'March' : 3,'April': 4,'May': 5,'June': 6,'July' : 7,'August': 8, 'September': 9, 'October': 10, 'November' : 11, 'December': 12}

    soup = bs.BeautifulSoup(websource)
    table = soup.find(lambda tag: tag.name=='table' and tag.has_key('id') and tag['id']=="calendar")
    temp = table.findAll('span')
    Mon, Year = temp[0].string.split()

    # insert starting day calendar-closed
    Mon = month2num.get(Mon)
    Mon = int(Mon)
    Year = int(Year)
    days_closed = table.findAll(lambda tag: tag.name=='td' and tag.has_key('class') and tag['class'] == 'calendar-closed')
    for i in days_closed:
        Day = int(i.text)
        date_temp = date(Year,Mon,Day).strftime("%m/%d/%Y")
        data_page[date_temp] = 0
    # insert following day calendar-fullday
    days_full = table.findAll(lambda tag: tag.name=='td' and tag.has_key('class') and tag['class'] == 'calendar-fullday')
    for i in days_full:
        Day = int(i.text)
        date_temp = date(Year,Mon,Day).strftime("%m/%d/%Y")
        data_page[date_temp] = 0
    # insert following day calendar-available
    days_available = table.findAll(lambda tag: tag.name=='td' and tag.has_key('class') and tag['class'] == 'calendar-available')

    for i in days_available:
        Day = int(i.text)
        date_temp = date(Year,Mon,Day).strftime("%m/%d/%Y")
        data_page[date_temp] = 1
    #print "==========================================="
    #print data_page
    return data_page

def creat_sqlite(Allowed_Days_Dict):
    """
    creat sqlite of 90 allowed time with their availability

    input : Allowed_Days_Dict = {date : availability}
    """
    #connecting database and creating table availability
    conn = sqlite3.connect("development.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS availability""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS availability
                  (date text,av int) """)
    dictlist = []
    for key, value in Allowed_Days_Dict.iteritems():
        temp = [key,value]
        dictlist.append(temp)
    cursor.executemany("INSERT INTO availability VALUES (?,?)" ,dictlist)
    conn.commit()
    cursor.close()
    conn.close()


def sqlreading():
    pkl_file = open('myfile.pkl', 'rb')
    Allowed_Days_Dict_old = pickle.load(pkl_file)
    pkl_file.close()
    return Allowed_Days_Dict_old

def dictDiff(dictA,dictB):
    for key,val in dictA.iteritems():
        if ( val != dictB[key] ):
            return 1

def renewSQL(changed,Allowed_Days_Dict):
        if ( changed ):
            creat_sqlite(Allowed_Days_Dict)
            output = open('myfile.pkl', 'wb')
            pickle.dump(Allowed_Days_Dict, output)
            output.close()


if __name__ == "__main__":
    """
    method description :
    1.get four month available and unavailable days and then return as a dict
    2.dict to sqlite
    """

    #Assign URL for search
    #Appointment Locator
    #   Location Address
    #   2571 North Earl Rudder Freeway
    #   Bryan, TX 77803

    URL = 'https://booknow.securedata-trans.com/1qed83ds/'

    #four_months for result record
    Allowed_Days_Dict = dict()

    #  virtual display of FireFox
    display = Display(visible=0, size=(800, 600))
    display.start()

# now Firefox will run in a virtual display. 
# you will not see the browser.

    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get(URL)
    browser.find_element_by_xpath("//select[@name='service_id']/option[text()='Driving Test - Regular Car / Pick-up Truck']").click()

    source = browser.page_source
    Allowed_Days_Dict = htmltableGetinfomation(source,Allowed_Days_Dict)
    #get another 3 pages information
    for i in range(1,4):
        browser.execute_script("javascript:dosubmit1('no', 'yes', 'log_in')")
        source = browser.page_source
        Allowed_Days_Dict = htmltableGetinfomation(source,Allowed_Days_Dict)

    #print "==========================================="
    #print Allowed_Days_Dict
    browser.close()

    #reading in the old date dict
    Allowed_Days_Dict_old = sqlreading()
    changed = 0
    changed = dictDiff( Allowed_Days_Dict_old, Allowed_Days_Dict)
    renewSQL(changed,Allowed_Days_Dict)
    
    print "================update_10min Done==========================="

    exit(changed)
