from os import getcwd, chdir, getenv
from shutil import rmtree
import time

print("Changing Directory...")
time.sleep(1)
chdir(f"{getenv('LOCALAPPDATA')}/discord")
print("New Directory: {0}".format(getcwd()))
time.sleep(1)
print("Removing Files...")
try:
    rmtree('Code Cache')
    rmtree('Cache')
    rmtree("GPUCache")
except FileNotFoundError:
    pass
input("Done, Press Enter to Exit!")
