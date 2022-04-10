import os
import subprocess

# 1.5.1
# Audit
status, output = subprocess.getstatusoutput("journalctl | grep 'protection: active'")

# Remediation
# On 32 bit systems install a kernel with PAE support, no installation is required on 64 bit
# systems:
# If necessary configure your bootloader to load the new kernel and reboot the system.
# You may need to enable NX or XD support in your bios.
