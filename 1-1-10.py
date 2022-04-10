import os
import subprocess

# 1.1.10
# Level 2
# Audit
status, output = subprocess.getstatusoutput("findmnt /var")

# Remediation
if status != 0:
    print("*************Run Partition Script**************")

