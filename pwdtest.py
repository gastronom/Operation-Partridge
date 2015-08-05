#!/usr/bin/env python
import subprocess

pwd = "/bin/pwd "
cmd = []
cmd.append(pwd)
print(cmd)
ret = subprocess.check_call(cmd,shell=True)
print(ret)
