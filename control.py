import subprocess
from time import sleep

while True:
    
    process = subprocess.Popen(['ssh', '-R', '80:192.168.55.8:80','pi@localhost.run'],stdout=subprocess.PIPE)
    sleep(5)
    
    process.terminate()

    out, err = process.communicate()
    linia = str(out)
    f = open('url.txt','w')
    f.write(linia.split()[-1][:-4])
    f.close()
    
    process = subprocess.Popen(['git', 'add', 'url.txt'])
    process = subprocess.Popen(['git', 'commit', '-m','update'])
    process = subprocess.Popen(['git', 'push'])
    process = subprocess.Popen(['ssh', '-R', '80:192.168.55.8:80','pi@localhost.run'])
    sleep(900)
    process.terminate()
    
