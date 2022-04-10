import os
import subprocess

# 1.1.17
# Level 2
# Audit
status, output = subprocess.getstatusoutput("findmnt /home")

# Remediation
if status != 0:
    print("*************Run Partition Script**************")

#########################################################
# NODEV
# 1.1.18
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /home |  grep -v nodev")

# Remediation
if status1 == 0:
    os.system("sed -ie \"/\/home/s/$(grep '/home' /etc/fstab | awk '{{print $4}}')/$(grep '/home' /etc/fstab | awk '{{print $4}}'),{}/\" /etc/fstab".format('nodev'))
    os.system("mount -o remount,nodev /home")



