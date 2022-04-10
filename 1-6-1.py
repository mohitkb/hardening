import os
import subprocess

# 1.6.1.1
# Audit

status, output = subprocess.getstatusoutput("dpkg -s apparmor | grep -E '(Status:|not installed)'")

# Remediation
if status != 0:
    os.system("apt install apparmor -y")

# 1.6.1.2
# Audit

status1, output1 = subprocess.getstatusoutput("grep \"^\s*linux\" /boot/grub/grub.cfg | grep \"apparmor=1\"")
status2, output2 = subprocess.getstatusoutput("grep \"^\s*linux\" /boot/grub/grub.cfg | grep \"security=apparmor\"")

# Remediation
if status1 != 0 or status2 !=0:
    os.system("sed -ie '/GRUB_CMDLINE_LINUX=/s/\"\"/\"apparmor=1 security=apparmor\"/' /etc/default/grub")
    os.system("update-grub")
