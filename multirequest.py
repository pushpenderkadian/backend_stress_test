import subprocess
import os
cmdss=""
i=0
for subdir, dirs, files in os.walk('./'):
    for file in files:
        i+=1
        if file.startswith("users"):
            cmdss=cmdss+" python "+file+" &"
        if(i>=20):
            break

print(cmdss[:-1])
subprocess.run(cmdss[:-1], shell=True)