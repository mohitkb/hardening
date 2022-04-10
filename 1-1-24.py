import os
import subprocess

# 1.1.24
# Workstation Level 2
# Audit
status, output = subprocess.getstatusoutput("modprobe -n -v usb-storage | grep 'install /bin/true'")

# Remediation
if status != 0:
    os.system("touch /etc/modprobe.d/usb_storage.conf")
    os.system("echo 'install usb-storage /bin/true' >> /etc/modprobe.d/usb_storage.conf")
    os.system("rmmod usb-storage")

