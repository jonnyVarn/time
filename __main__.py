#/usr/bin/python3.7

import ntplib
from ntplib import ntp_to_system_time as ntp_to_system_time
import time
import os
import subprocess
from subprocess import Popen 
from subprocess import check_as run_cmd
from subprocess import check_

NIST='gbg1.ntp.se'
ntp= ntplib.NTPClient()
ntpResponse=ntp.request(NIST)

if (ntpResponse):
    correct_time=int(ntpResponse.recv_time)
    correct_time=str(correct_time)
    #correct_time=" @"+correct_time+" "
    print(correct_time)
    run_cmd(["date" ,"-d", "@",correct_time], shell=True)
    print(correct_time)
    #newest_time=(ntpResponse)
    run_cmd=("date")
    



