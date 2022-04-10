import os
import subprocess

# 1.8.2
# Audit
#status, output = subprocess.getstatusoutput("sed -n -e '/\[org\/gnome\/login-screen\]/,/\[org\/gnome\/settings-daemon\/plugins\/power\]/ p' /etc/gdm3/greeter.dconf-defaults | grep \"^banner-message-enable=true\"")
status1, output1 = subprocess.getstatusoutput("cat /etc/gdm3/greeter.dconf-defaults | grep -E \"^banner-message-enable=true\"")
status2, output2 = subprocess.getstatusoutput("cat /etc/gdm3/greeter.dconf-defaults | grep -E \"^banner-message-text=\"")

# Remediation
if status1 != 0:
    os.system("sed -ie \"/banner-message-enable/s/^# //\" /etc/gdm3/greeter.dconf-defaults")

if status2 != 0:
    os.system("sed -ie \"/banner-message-text/s/^# //\" /etc/gdm3/greeter.dconf-defaults")

os.system("dpkg-reconfigure gdm3")

# 1.8.3
# Audit
status, output = subprocess.getstatusoutput("grep -E \"^disable-user-list=true\" /etc/gdm3/greeter.dconf-defaults")

# Remediation
if status != 0:
    os.system("sed -ie \"/disable-user-list=true/s/^# //\" /etc/gdm3/greeter.dconf-defaults")
    os.system("dpkg-reconfigure gdm3")

# 1.8.4
# Audit
status, output = subprocess.getstatusoutput("grep -Eis '^\s*Enable\s*=\s*true' /etc/gdm3/custom.conf")

# Remediation
if status == 0:
    os.system("sed -ie \"/Enable=true/s/.*//\" /etc/gdm3/custom.conf")
    os.system("dpkg-reconfigure gdm3")
