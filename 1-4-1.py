import os
import subprocess

# 1.4.1
# Audit
status, output =subprocess.getstatusoutput("grep -E '^\s*chmod\s+[0-7][0-7][0-7]\s+\$\{grub_cfg\}\.new' /usr/sbin/grub-mkconfig | awk '{print $2}'")

# Remediation
if output != 400:
    os.system("sed -ri 's/ && ! grep \"\^password\" \$\{grub_cfg\}.new >\/dev\/null//' /usr/sbin/grub-mkconfig")
    os.system("sed -ri 's/chmod\s+[0-7][0-7][0-7]\s+\$\{grub_cfg\}\.new/chmod 400 ${grub_cfg}.new/' /usr/sbin/grub-mkconfig")

