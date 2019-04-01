import re,threading
import time,datetime,os
from datetime import datetime
from time import sleep
array1=[]
array2=[]
array3=[]
sample1=r"Name.(.*).Birthdaydate.(.*).Alarmtime.(.*)"
p=open("birthdaydetails.txt","r")
lines=p.readlines()
for line in lines:
    match=re.search(sample1,line,re.M|re.I)
    if match!=None:
        a=str(match.group(1))
        b=str(match.group(2))
        c=str(match.group(3))
        array1.append(a)
        array2.append(b)
        array3.append(c)
      
def Alarm():
 while True:
        for i in array2:
            j=str(time.strftime("%x"))
            if i==j:
                k=str(datetime.time(datetime.now()).replace(second=0, microsecond=0))
                for h,l in zip(array3,array1):
                      if h==k:
                          os.system('notify-send "Birthdays Today: ' + l+'"')
                          print "done"
                      sleep(8)    

if __name__=="__main__":

        print "threading started"
        t1=threading.Thread(target=Alarm)
        t1.start()
        t1.join()
        
        print "threading done"                  
