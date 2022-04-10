#!/bin/bash

apt install xfsprogs -y
modprobe -v xfs
grep xfs /proc/filesystems

if echo '$?' == 0
then
  if lsblk | grep '^sdc.*5G'
  then
    fdisk /dev/sdb <<EOF
g
n



w
EOF

    fdisk /dev/sdc <<EOF
g
n


+500M
n


+500M
n


+500M
n


+500M
w
EOF

    mkfs.xfs /dev/sdb1
    mkfs.xfs /dev/sdc1
    mkfs.xfs /dev/sdc2
    mkfs.xfs /dev/sdc3
    mkfs.xfs /dev/sdc4

    mkdir /backup
    mkdir -p /var/tmp
    mkdir -p /var/log
    mkdir -p /var/log/audit

    cp -r /var /backup/
    cp -r /home /backup/


    echo '/dev/sdb1 /var xfs defaults 0 0' >> /etc/fstab
    echo '/dev/sdc2 /var/tmp xfs defaults 0 0' >> /etc/fstab
    echo '/dev/sdc3 /var/log xfs defaults 0 0' >> /etc/fstab
    echo '/dev/sdc4 /var/log/audit xfs defaults 0 0' >> /etc/fstab
    echo '/dev/sdc5 /home xfs defaults 0 0' >> /etc/fstab


    mount -t xfs /dev/sdb1 /var
    cp -r /backup/var/* /var

    mount -t xfs /dev/sdc1 /var/tmp
    cp -r /backup/var/tmp/* /var/tmp

    mount -t xfs /dev/sdc2 /var/log
    cp -r /backup/var/log/* /var/log

    mount -t xfs /dev/sdc3 /var/log/audit
    cp -r /backup/var/log/audit/* /var/log/audit

    mount -t xfs /dev/sdc4 /home
    cp -r /backup/home/* /home


  else
    echo "Add disk sdb & sdc 5 GB"
  fi
else
  echo "Check Internet"
fi

