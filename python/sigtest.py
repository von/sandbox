#!/usr/bin/env python3
#
# Demononstrat signals and that a SIGINT doesn't kill a chld thread
#
import getpass
import os
import signal
import time
from threading import Thread

class PassReader(Thread):
    def run(self):
        print("Don't enter a password, just wait...")
        password = getpass.getpass()
        print(password)

class Killer(Thread):
    def run(self):
        time.sleep(3)
        print("Sending SIGKILL to  myself...")
        os.kill(os.getpid(), signal.SIGKILL)

p = PassReader()
p.start()

p2 = Killer()
p2.start()

time.sleep(1)
print("Sending SIGINT to  myself...")
os.kill(os.getpid(), signal.SIGINT)
