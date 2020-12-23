#!/usr/bin/python3
import ntplib
from ntplib import ntp_to_system_time as ntp_to_system_time
import time
import os
import subprocess
from subprocess import Popen as Popen
from subprocess import check_output as check_output
from subprocess import call as run_cmd

ntp0 = 'gbg2.ntp.se'
ntp1= 'gbg1.ntp.se'
ntp = ntplib.NTPClient()
ntpResponse = ntp.request(ntp0)

if (ntpResponse):
    correct_time = int(ntpResponse.recv_time)
    correct_time = str(correct_time)
    correct_time_str="@" +correct_time
    print("------")
    print(correct_time_str)
    print("----")
    annan=check_output(["/usr/bin/date", "-d", correct_time_str])
    Popen(["/usr/bin/date", "-d", correct_time_str], shell=True)
    annan2=annan.decode()
    print(annan2)
    print("--------------------------------")
    
    file=open('time.sh', 'w+')
    file.write("#!/usr/bin/bash \n"
    "### BEGIN INIT INFO + \n"
    "# Provides:          timecheck program \n"
    "# Required-Start: \n"
    "# Required-Stop:     $local_fs \n" 
    "# Default-Start:     2 3 4 5 \n"
    "# Default-Stop:      0 1 6 \n"
    "# Short-Description: time_correct \n"
    "# Description:       time_correct \n"
    "### END INIT INFO\t") 
    file.write("date -d "  +correct_time_str)
    file.close()
    Popen(["sudo","chmod", "+x", "time.sh"])
    Popen(["cp", "time.sh", "/etc/init.d/time.sh"])
    #os.chmod(/etc/init.d/time.sh, 755)
    Popen(["chmod", "+x", "/etc/init.d/time.sh"])
    #os.chmod(/etc/init.d/time.sh, 755)

    Popen(["service", "time.sh", "start"])
    #Popen(["sudo","chmod", "u+s", "time.sh"])
    os.chmod("time.sh", 755)
    #Popen(["bash", "/home/jonny/time/time.sh"], shell=True)
    run_cmd("date")
    print("date should be corrected")
    #choice=input("do you wish to create a service? yes or else nothing")
    #if choice=="yes":
        #init==("input are you using init or system d?")
        #if init==" init":
            #print("cool will do that later")
