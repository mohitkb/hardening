##########  Incomplete ###############
import os
import subprocess

# 1.4.2
# Audit
status, output =subprocess.getstatusoutput("grep \"^set superusers\" /boot/grub/grub.cfg")
status1, output1 =subprocess.getstatusoutput("grep \"^password\" /boot/grub/grub.cfg")
# Remediation
if  != 0:

