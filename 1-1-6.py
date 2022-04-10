import subprocess
import os

# 1.1.6
# Audit
status, output = subprocess.getstatusoutput("findmnt -n /dev/shm")

# If not present in fstab
response = os.system("grep -q '/dev/shm ' /etc/fstab")
if response != 0:
    os.system("echo 'none /dev/shm tmpfs rw,noexec,nosuid,nodev 0 0' >> /etc/fstab")
    os.system("mount -o remount,noexec,nodev,nosuid /dev/shm")
# else:
    # os.system("grep '/dev/shm ' /etc/fstab | sed -i 's//' /etc/fstab")

# Remediation
# if status != 0:
    # Not Complete ( ^ Solution can be used)
    # os.system("grep '/dev/shm ' /etc/fstab | awk '{ gsub (\".*\",\"lol\",$4); print $4}'")

########################################################
# NODEV
# 1.1.7
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /dev/shm |  grep -v nodev")

# Remediation
if status1 == 0:
    os.system("sed -ie \"/\/dev\/shm/s/$(grep '/dev/shm' /etc/fstab | awk '{{print $4}}')/$(grep '/dev/shm' /etc/fstab | awk '{{print $4}}'),{}/\" /etc/fstab".format('nodev'))
    os.system("mount -o remount,noexec,nodev,nosuid /dev/shm")


#########################################################
# NOSUID
# 1.1.8
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /dev/shm |  grep -v nosuid")

# Remediation
if status1 == 0:
    os.system("sed -ie \"/\/dev\/shm/s/$(grep '/dev/shm' /etc/fstab | awk '{{print $4}}')/$(grep '/dev/shm' /etc/fstab | awk '{{print $4}}'),{}/\" /etc/fstab".format('nosuid'))
    os.system("mount -o remount,noexec,nodev,nosuid /dev/shm")

########################################################
# NOEXEC
# 1.1.9
# Audit
status1, output1 = subprocess.getstatusoutput("findmnt -n /dev/shm |  grep -v noexec")

# Remediation
if status1 == 0:
    os.system("sed -ie \"/\/dev\/shm/s/$(grep '/dev/shm' /etc/fstab | awk '{{print $4}}')/$(grep '/dev/shm' /etc/fstab | awk '{{print $4}}'),{}/\" /etc/fstab".format('noexec'))
    os.system("mount -o remount,noexec,nodev,nosuid /dev/shm")


#####--------awk -F ',' '/Options/{print}' tmp.mount-------------
