# 1.1.1 Disable unused filesystems

import subprocess
import os

file = open("temp.txt","a+")
FS = ["cramfs", "freevxfs", "jffs2", "hfs", "hfsplus", "udf"]
#fixed = subprocess.getoutput("/usr/sbin/modprobe -n -v cramfs | grep 'install /bin/true'")
for g in FS:
    print(g)
    status, output = subprocess.getstatusoutput("/usr/sbin/modprobe -n -v {} | grep 'install /bin/true'".format(g, g))
    print(output)
    #print(status)

    if status == 0:
        print("No Change")
        print("---------------------")
    else:
        file.write("{}\n".format(g))
        print("---------------------")


file.close()

#####################################################

#Remediation

file = open("temp.txt", "r")
f = open("/etc/modprobe.d/disablefs.conf", "a+")

for g in file.readlines():
    x = g.strip('\n')
    print(x)
    f.write("install {} /bin/true \n".format(x))
    os.system("rmmod {}".format(x))


f.close()
file.close()


