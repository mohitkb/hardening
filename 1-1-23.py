import os
import subprocess

# 1.1.23
# Workstation Level 2
# Audit
status, output = subprocess.getstatusoutput("systemctl is-enabled autofs")
status1, output1 = subprocess.getstatusoutput("dpkg -s autofs >2 temp.txt")

# Remediation
if output == 'enabled':
    os.system("systemctl --now disable autofs")

if status1 == 0:
    os.system("apt purge autofs")