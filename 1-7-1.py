import os
import subprocess

# 1.7.1
# Audit

status, output = subprocess.getstatusoutput("grep -Eis \"(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/\"//g'))\" /etc/motd")

# Remediation
if status == 0:
    os.system("rm /etc/motd")

# 1.7.2
# Audit

status, output = subprocess.getstatusoutput("grep -E -i \"(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/\"//g'))\" /etc/issue")

# Remediation
if status == 0:
    os.system("echo \"Authorized uses only. All activity may be monitored and reported.\" > /etc/issue")

# 1.7.3
# Audit

status, output = subprocess.getstatusoutput("grep -E -i \"(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/\"//g'))\" /etc/issue.net")

# Remediation
if status == 0:
    os.system("echo \"Authorized uses only. All activity may be monitored and reported.\" > /etc/issue.net")

# 1.7.4
# Audit

status, output = subprocess.getstatusoutput("stat -L /etc/motd")

# Remediation
if status == 0:
    os.system("rm /etc/motd")

# 1.7.5
# Audit
status, output = subprocess.getstatusoutput("stat -L /etc/issue | grep \"Access: (\" |  awk '{print $2}' | sed 's/\/.*)//' | sed 's/(//' | grep -oE \".{3}$\"")
status1, output1 = subprocess.getstatusoutput("stat -L /etc/issue | grep \"Access: (\" | sed 's/ //g' | awk -F \"(\" '{print $3}' | sed 's/).*//'")
status2, output2 = subprocess.getstatusoutput("stat -L /etc/issue | grep \"Access: (\" | sed 's/ //g' | awk -F \"(\" '{print $4}' | sed 's/).*//'")

# Remediation
if output != 644:
    os.system("chmod u-x,go-wx $(readlink -e /etc/issue)")

if output1 != "0/root" and output2 != "0/root":
    os.system("chown root:root $(readlink -e /etc/issue)")

# 1.7.6
# Audit
status, output = subprocess.getstatusoutput("stat -L /etc/issue.net | grep \"Access: (\" |  awk '{print $2}' | sed 's/\/.*)//' | sed 's/(//' | grep -oE \".{3}$\"")
status1, output1 = subprocess.getstatusoutput("stat -L /etc/issue.net | grep \"Access: (\" | sed 's/ //g' | awk -F \"(\" '{print $3}' | sed 's/).*//'")
status2, output2 = subprocess.getstatusoutput("stat -L /etc/issue.net | grep \"Access: (\" | sed 's/ //g' | awk -F \"(\" '{print $4}' | sed 's/).*//'")

# Remediation
if output != 644:
    os.system("chmod u-x,go-wx $(readlink -e /etc/issue.net)")

if output1 != "0/root" and output2 != "0/root":
    os.system("chown root:root $(readlink -e /etc/issue.net)")
