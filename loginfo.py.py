#!/usr/bin/env python3
# import the module os to interact with the file system.

import os 

# assign variable pr1 to the output of awk(print the line that dose not have my ip address)
pr1 = " awk '!/192.168.58.137/{print}'"

# assign the varaible info_log to the output of the command (sudo sudo pinky -f | %s >> loginfo.txt)
info_log = os.popen("sudo pinky -f | %s >> loginfo.txt" %pr1).read()

# if the output of the command is empty pass
if(info_log ==""):
    pass

# else cat the loginfo file and send it to my email
else:
    os.system("cat loginfo.txt | mail -s 'Login Alert' ahmed@192.168.58.137")