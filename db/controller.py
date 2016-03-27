#now close checkAvailibility
import checkAvailibility
import update_10min
from datetime import date, time, datetime, timedelta
from subprocess import *

"""
data={"03/31/2016":0,
      "04/01/2016":1,
      "04/02/2016":1,
      "04/03/2016":0}
"""

#checkAvailibility.checkAvailibility(data)

#start up


##first time initialize!!!
p =Popen('./update_day.py')  

now=datetime.now()
strnow = now.strftime('%Y-%m-%d %H:%M:%S')
print ("now:",strnow)#can be deleted 1
# First next run time
period = timedelta(days=0, hours=0, minutes=0, seconds=30)
next_time = now + period
strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
print ("next run:",strnext_time)#can be deleted 2


#current date
str_record_date=now.strftime('%m/%d/%Y')

while True:
    # Get system current time
    iter_now = datetime.now()
    iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
    iter_now_date=iter_now.strftime('%m/%d/%Y')
    
    #if str(iter_now_time) == str(strnext_time) :
    if str(iter_now_time) == str(strnext_time) :
        #get every start work time
        print ("start work: %s" % iter_now_time)
    
        #call task func
        q =Popen('./update_10min.py',stdin=PIPE,stdout=PIPE)
        print q.stdout.readline()  
    
        #call update_10min routine
        data = update_10min.sqlreading()
        checkAvailibility.checkAvailibility(data)
        print ("task done.")
        
        #get next iterate time
        iter_time=iter_now+period
        strnext_time=iter_now+period
        strnext_time=iter_time.strftime('%Y-%m-%d %H:%M:%S')
        print ("next_iter:%s" % strnext_time)
        #continue next iteration
        if str(iter_now_date)!=str(str_record_date):
            str_record_date=iter_now_datez
            print "A New Day!"
            p =Popen('./update_day.py') 
		


