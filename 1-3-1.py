import os
import subprocess

# 1.3.1
# Audit
status, output = subprocess.getstatusoutput("dpkg -s aide | grep 'ok installed'")
status1, output1 = subprocess.getstatusoutput("dpkg -s aide-common | grep 'ok installed'")

# Remediation
if status != 0:
    os.system("apt install aide")

if status1 != 0:
    os.system("apt install aide-common")


#####    Aide Initialization   #####
# aideinit
# mv /var/lib/aide/aide.db.new /var/lib/aide/aide.d

