#!/usr/bin/python3.7
import ntplib
from ntplib import ntp_to_system_time as ntp_to_system_time
import time
import os
import subprocess
from subprocess import Popen as Popen
from subprocess import check_output as check_output
from subprocess import call as run_cmd

NIST = 'gbg2.ntp.se'
ntp = ntplib.NTPClient()
ntpResponse = ntp.request(NIST)

if (ntpResponse):
    correct_time = int(ntpResponse.recv_time)
    correct_time = str(correct_time)
    #correct_time=" @"+correct_time+" "
    print(correct_time)
    #run_cmd(["date", "-d", "@", correct_time], shell=True)
    Popen(["date", "-d", " @"+correct_time], shell=True)
    nisse=check_output(["date", "-d", " @", correct_time,], shell=True)
    print("--------------------------------")
    print(nisse)
    print("--------------------------------")
    print(correct_time)
    # newest_time=(ntpResponse)
    run_cmd(["date"])
    
    file=open('time.sh', 'w+')
    correct_time="\""+correct_time+"\""
    file.write("date -d " +"@" +str(correct_time))
    file.close()
    Popen(["sudo","chmod", "+x", "/home/jonny/time/time.sh"])
    Popen(["sudo", "/home/jonny/time/time.sh"])
    os.chmod("/home/jonny/time/time.sh", 755)
    Popen(["bash", "/home/jonny/time/time.sh"])

    #run_cmd("date")

