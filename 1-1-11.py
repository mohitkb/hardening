import os
import subprocess

# 1.1.11
# Level 2
# Audit
status, output = subprocess.getstatusoutput("findmnt /var/tmp")

# Remediation
if status != 0:
    os.system("echo 'none /var/tmp tmpfs rw,noexec,nosuid,nodev 0 0' >> /etc/fstab")
    os.system("mount -o remount,noexec,nodev,nosuid /var/tmp")
    print("*************Run Partition Script for Level 2**************")

#########################################################
# NODEV
# 1.1.12
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /var/tmp |  grep -v nodev")

# Remediation
if status1 == 0:
    os.system("sed -ie \"/\/var\/tmp/s/$(grep '/var/tmp' /etc/fstab | awk '{{print $4}}')/$(grep '/var/tmp' /etc/fstab | awk '{{print $4}}'),{}/\" /etc/fstab".format('nodev'))
    os.system("mount -o remount,noexec,nodev,nosuid /var/tmp")


#########################################################
# NOSUID
# 1.1.13
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /var/tmp |  grep -v nosuid")

# Remediation
if status1 == 0:
    os.system("sed -ie \"/\/var\/tmp/s/$(grep '/var/tmp' /etc/fstab | awk '{{print $4}}')/$(grep '/var/tmp' /etc/fstab | awk '{{print $4}}'),{}/\" /etc/fstab".format('nosuid'))
    os.system("mount -o remount,noexec,nodev,nosuid /var/tmp")

########################################################
# NOEXEC
# 1.1.14
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /var/tmp |  grep -v noexec")

# Remediation
if status1 == 0:
    os.system("sed -ie \"/\/var\/tmp/s/$(grep '/var/tmp' /etc/fstab | awk '{{print $4}}')/$(grep '/var/tmp' /etc/fstab | awk '{{print $4}}'),{}/\" /etc/fstab".format('noexec'))
    os.system("mount -o remount,noexec,nodev,nosuid /var/tmp")


