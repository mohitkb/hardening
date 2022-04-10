import os
import subprocess

# 1.9
# Audit
status, output = subprocess.getstatusoutput("apt -s upgrade | grep upgraded | awk '{print $1}'")

# Remediation
if output != 0:
    os.system("apt upgrade -y")