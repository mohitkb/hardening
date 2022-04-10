import os
import subprocess

# 1.5.3
# Audit

status, output = subprocess.getstatusoutput("dpkg -s prelink")

# Remediation
if status == 0:
    os.system("prelink -ua")
    os.system("apt purge prelink")

