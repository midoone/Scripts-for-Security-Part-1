#!/usr/bin/env python3
# import the module os to interact with the file system.
# import the moudule time to put the program in sleep.
import os
import time

# assign the varaible folder_1 to the pacth /var/log
folder_1 = "/var/log"

# put the code in sleep for 2.4 s and then restart it
time.sleep(2.4)

# assign the variable folder 2 to the same patch to check if any change was made.
folder_2 = "/var/log"

#assign vraiable Dir to the out put of command sudo diff between folder_1 and floder_1
Dir = os.popen("sudo diff %s %s >> log.txt" %(folder_1,folder_2)).read()

# if the the output of Dir empty pass
if (Dir == ""):
    pass

# else copy the output of the command to file called log.txt
# and then send the notification to my email
else:
    os.system("sudo diff %s %s >> log.txt" %(folder_1,folder_2))
    os.system("cat log.txt| mail -s 'Change Alert in Log' ahmed@192.168.58.137")