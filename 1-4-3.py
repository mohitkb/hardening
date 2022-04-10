import os
import subprocess

# 1.4.3
# Audit

status, output = subprocess.getstatusoutput("stat /boot/grub/grub.cfg | grep \"Access: (\" |  awk '{print $2}' | sed 's/\/.*)//' | sed 's/(//' | grep -oE \".{3}$\"")
status1, output1 = subprocess.getstatusoutput("stat /boot/grub/grub.cfg | grep \"Access: (\" | sed 's/ //g' | awk -F \"(\" '{print $3}' | sed 's/).*//'")
status2, output2 = subprocess.getstatusoutput("stat /boot/grub/grub.cfg | grep \"Access: (\" | sed 's/ //g' | awk -F \"(\" '{print $4}' | sed 's/).*//'")

# Remediation
if output != 400:
    os.system("chmod u-wx,go-rwx /boot/grub/grub.cfg")

if output1 != "0/root" and output2 != "0/root":
    os.system("chown root:root /boot/grub/grub.cfg")
