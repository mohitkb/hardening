import subprocess
import os

# 1.1.2
# Audit
status, output = subprocess.getstatusoutput("findmnt -n /tmp")

# Remediation
if status != 0:
    os.system("cp -v /usr/share/systemd/tmp.mount /etc/systemd/system/")
    # os.system("grep 'Options=' /etc/systemd/system/tmp.mount | sed -i 's/Options.*/Options=mode=1777,strictatime,nosuid,nodev,noexec/g' /etc/systemd/system/tmp.mount")
    os.system("systemctl daemon-reload")
    os.system("systemctl --now enable tmp.mount")

########################################################
# NODEV
# 1.1.3
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /tmp |  grep -v nodev")

# Remediation
if status1 == 0:
    os.system("sed -i 's/Options=.*/Options=mode=1777,strictatime,noexec,nodev,nosuid/' /etc/systemd/system/tmp.mount")
    # os.system("mount -o remount,nodev /tmp")
    os.system("systemctl daemon-reload")
    os.system("systemctl reload tmp.mount")

########################################################
# NOSUID
# 1.1.4
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /tmp |  grep -v nosuid")

# Remediation
if status1 == 0:
    os.system("sed -i 's/Options=.*/Options=mode=1777,strictatime,noexec,nodev,nosuid/' /etc/systemd/system/tmp.mount")
    # os.system("mount -o remount,nosuid /tmp")
    os.system("systemctl daemon-reload")
    os.system("systemctl reload tmp.mount")

########################################################
# NOEXEC
# 1.1.5
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /tmp |  grep -v noexec")

# Remediation
if status1 == 0:
    os.system("sed -i 's/Options=.*/Options=mode=1777,strictatime,noexec,nodev,nosuid/' /etc/systemd/system/tmp.mount")
    #os.system("mount -o remount,noexec /tmp")
    os.system("systemctl daemon-reload")
    os.system("systemctl reload tmp.mount")

#####--------awk -F ',' '/Options/{print}' tmp.mount-------------
