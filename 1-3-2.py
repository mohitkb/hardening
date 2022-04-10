import os
import subprocess
import time

# 1.3.2
# Audit
status, output = subprocess.getstatusoutput("systemctl is-enabled aidecheck.service")
status1, output1 = subprocess.getstatusoutput("systemctl is-enabled aidecheck.timer")
status2, output2 = subprocess.getstatusoutput("systemctl status aidecheck.timer")

os.system("systemctl unmask aidecheck.service")
os.system("systemctl unmask aidecheck.timer")

# Remediation
if status != 0:
    os.system("touch /etc/systemd/system/aidecheck.service")
    f_service = open("/etc/systemd/system/aidecheck.service", "a+")
    f_service.write('''[Unit]
Description=Aide Check

[Service]
Type=simple
ExecStart=/usr/bin/aide.wrapper --config /etc/aide/aide.conf --check

[Install]
WantedBy=multi-user.target''')
    f_service.close()
else:
    print("Nothing")
if status1 != 0:
    os.system("touch /etc/systemd/system/aidecheck.timer")
    f_timer = open("/etc/systemd/system/aidecheck.timer", "a+")
    f_timer.write('''[Unit]
Description=Aide check every day at 5AM

[Timer]
OnCalendar=*-*-* 05:00:00
Unit=aidecheck.service

[Install]
WantedBy=multi-user.target''')
    f_timer.close()
else:
    print("Nothing")


os.system("chown root:root /etc/systemd/system/aidecheck.*")

os.system("chmod 0644 /etc/systemd/system/aidecheck.*")


os.system("systemctl daemon-reload")

os.system("systemctl unmask aidecheck.service")

os.system("systemctl unmask aidecheck.timer")

os.system("systemctl enable aidecheck.service")

os.system("systemctl --now enable aidecheck.timer")




