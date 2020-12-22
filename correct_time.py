#!/usr/bin/python3.7
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
    #Popen(["date", "-d", correct_time], shell=True)
    #nisse=check_output(["date", "-d", " @", correct_time,], shell=True)
    #print("--------------------------------")
    #print(nisse)
    print("--------------------------------")
    #print(correct_time)
    #newest_time=(ntpResponse)
    #run_cmd(["date"])
    
    file=open('time.sh', 'w+')
    file.write("date -d "  +correct_time_str)
    file.close()
    Popen(["sudo","chmod", "+x", "/home/jonny/time/time.sh"])
    Popen(["sudo","chmod", "u+s", "/home/jonny/time/time.sh"])
    os.chmod("/home/jonny/time/time.sh", 755)
    Popen(["bash", "/home/jonny/time/time.sh"], shell=True)

    run_cmd("date")
    print("date should be corrected")
    choice=input("do you wish to create a service? yes or else nothing")
    if choice=="yes":
        init==("input are you using init or system d?")
        if init==" init":
            print("cool will do that later")

    



