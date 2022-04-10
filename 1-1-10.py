import os
import subprocess

# 1.1.10
# Level 2
# Audit
status, output = subprocess.getstatusoutput("findmnt /var")

# Remediation
if status != 0:
    os.system("echo 'none /var tmpfs rw,noexec,nosuid,nodev 0 0' >> /etc/fstab")
    os.system("mount -o remount,noexec,nodev,nosuid /var")
    print("*************Run Partition Script for Level 2**************")

