import os
import subprocess

# 1.1.16
# Level 2
# Audit
status, output = subprocess.getstatusoutput("findmnt /var/log/audit")

# Remediation
if status != 0:
    print("*************Run Partition Script**************")




