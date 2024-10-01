import subprocess
output = subprocess.check_output(("arp", "-a"))
# Parse output here
output.pars